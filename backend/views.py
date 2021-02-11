from django.shortcuts import render, redirect
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing import image
import argparse, time, cv2, imutils, datetime, os
from imutils.video import VideoStream
from .models import Captured_Images, User_Profile_Images
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

#  Create your views here.
username = ""
context = {}

def handle_image_upload(f, sub_location):
    i = datetime.datetime.now()
    now = str(i.year) + "-" + str(i.month) + "-" + str(i.day) + "-" + \
        str(i.hour) + "-" + str(i.minute) + "-" + \
        str(i.second)
    filenaam = "media/" + str(sub_location) + "/" + str(now) + str(f.name)
    destination = open('media/' + str(sub_location) + '/%s' % f.name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    os.rename('media/' + str(sub_location) + '/%s' % f.name, filenaam)
    filenaam = '/' + filenaam
    return(filenaam)

def welcome(request):
    if request.user.is_active:
        return redirect("home")
    return render(request, "welcome.html")

def login(request): 
    global context
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("Logged in")
            return render(request, "home.html", {"username": username})
        elif username == "" and password == "":
            context["message"] = "Please enter your username and password"
            return render(request, "login.html", context)
        else:
            context["message"] = "Invalid login credentials"
            return render(request, "login.html", context)
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('welcome')

def signup(request):
    global username
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        re_password = request.POST['re_password']
        email = request.POST['email']
        user_profile_img = request.FILES.get("user_profile_img", None)
        print(user_profile_img)
        username = first_name
        if password == re_password:
            if User.objects.filter(username=username).exists():
                context = {'message': 'username already taken'}
                messages.info(request, 'Username taken')
                return render(request, 'signup.html', context)
            elif User.objects.filter(email=email).exists():
                context = {'message': 'Email ID already taken'}
                messages.info(request, 'Email ID taken')
                return render(request, 'signup.html', context)
            else:
                if user_profile_img != None:
                    user_profile = handle_image_upload(user_profile_img, "user_profile_images")
                    user = User.objects.create_user(
                        username=username, 
                        password=password, 
                        email=email, 
                        first_name=first_name, 
                        last_name=last_name 
                        )
                    user.save()
                    user_img = User_Profile_Images(user_id_id=User.objects.get(username=username).id, user_img=user_profile)
                    user_img.save()
                    auth.login(request, user)
                    return render(request, "home.html", {'username': username})
                else:
                    user_profile_img = "media/user_profile_images/icons8-user-100.png"
                    user = User.objects.create_user(
                        username=username, 
                        password=password, 
                        email=email, 
                        first_name=first_name, 
                        last_name=last_name
                        )
                    user.save()
                    user_img = User_Profile_Images(user_id_id=User.objects.get(username=username).id, user_img=user_profile_img)
                    user_img.save()
                    auth.login(request, user)
                    return render(request, "home.html", {'username': username})
    return render(request, "signup.html")

def home(request):
    if request.user.is_authenticated:
        user = request.user.username
        return render(request, "home.html", {'username': user})

def account(request):
    if request.user.is_authenticated:
        if request.user.is_active:
            id = request.user.id
            user_profile = User_Profile_Images.objects.filter(user_id_id=id)
    return render(request, "account.html", {"profile_pic": user_profile})


def detectface(request):
    dt = datetime.datetime.now()
    dt = dt.strftime("%d/%m/%Y%H:%M:%S")
    print("[INFORMATION] Loading model... ")
    classifier = load_model('EmotionDetectionModel.h5')
    net = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel")
    class_labels=['Angry','Happy','Neutral','Sad','Surprise']
    print("[INFORMATION] Starting Video Stream... ")
    vs = VideoStream(src=0).start()
    time.sleep(1)
    p = []
    while True:
        fram = vs.read()
        fram = imutils.resize(fram, width=800)
        # grab frame dimensions and convert it to a blob
        (h, w) = fram.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(fram, (300, 300)), 1.0, (300,300), (104.0, 177.0, 123.0))
        net.setInput(blob)
        detections = net.forward()
        # loop over the detections
        for i in range(0, detections.shape[2]):
            labels=[]
            # extract confidence
            confidence = detections[0, 0, i, 2]
            if confidence < 0.7:
                continue
            
            # compute x and y coordinates of the bounding box for the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, StartY, endX, endY) = box.astype("int")
            
            # draw the bounding boxes
            cv2.rectangle(fram, (startX, StartY), (endX, endY), (0, 0, 255), 2)
            gray = cv2.cvtColor(fram, cv2.COLOR_BGR2GRAY)
            roi_gray=gray[StartY:endX,startX:endY]
            roi_gray=cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)
            roi=roi_gray.astype('float')/255.0
            roi=img_to_array(roi)
            roi=np.expand_dims(roi,axis=0)
            y = StartY - 10 if StartY - 10 > 10 else StartY + 10
            p = cv2.rectangle(fram, (startX, StartY), (endX, endY), (0, 0, 255), 2)
            preds=classifier.predict(roi)[0]
            label=class_labels[preds.argmax()]
            # print(label)
            label_position=(startX,y)
            cv2.putText(fram,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        if np.any(p):
            i = datetime.datetime.now()
            now = str(i.year) + '-' + str(i.month) + '-' + str(i.day) + '-' + str(i.day) + '-' + str(i.hour) + '-' + str(i.minute) + '-' + str(i.second)
            filenaam = 'media/user_images/' + "user" + str(now) + '.jpg'
            destination = open(filenaam, 'w+')
            main_pic = cv2.imwrite(filenaam, fram)
            destination.close()
            break
    # ending all processes
    vs.stop()
    cap = Captured_Images(user_face_image = filenaam)
    cap.save()
    return render(request, "home.html", {'emotion':label})

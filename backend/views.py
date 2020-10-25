from django.shortcuts import render, redirect
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing import image
import argparse, time, cv2, imutils, datetime, os
from imutils.video import VideoStream
from .models import Captured_Images

# Create your views here.

def welcome(request):
    return render(request, "welcome.html")

def login(request): 
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def home(request):
    return render(request, "home.html")

def account(request):
    return render(request, "account.html")


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
            label_position=(startX,y)
            cv2.putText(fram,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        if np.any(p):
            i = datetime.datetime.now()
            now = str(i.year) + '-' + str(i.month) + '-' + str(i.day) + '-' + str(i.day) + '-' + str(i.hour) + '-' + str(i.minute) + '-' + str(i.second)
            filenaam = 'media/' + "user" + str(now) + '.jpg'
            destination = open(filenaam, 'w+')
            main_pic = cv2.imwrite(filenaam, fram)
            destination.close()
            break
    # ending all processes
    vs.stop()
    cap = Captured_Images(user_face_image = filenaam)
    cap.save()
    return redirect('home')

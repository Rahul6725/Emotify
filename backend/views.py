from django.shortcuts import render, redirect
import numpy as np
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
    net = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel")
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
            # extract confidence
            confidence = detections[0, 0, i, 2]
            if confidence < 0.7:
                continue
            # compute x and y coordinates of the bounding box for the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, StartY, endX, endY) = box.astype("int")
            # draw the bounding boxes
            text = "{:2f}%".format(confidence * 100)
            y = StartY - 10 if StartY - 10 > 10 else StartY + 10
            p = cv2.rectangle(fram, (startX, StartY), (endX, endY), (0, 0, 255), 2)
            cv2.rectangle(fram, (startX, StartY), (endX, endY), (0, 0, 255), 2)
            cv2.putText(fram, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
        # cv2.imshow("Frame", fram)
        # key = cv2.waitKey(i) & 0xFF
        # show the output frame
        if np.any(p):
            i = datetime.datetime.now()
            now = str(i.year) + '-' + str(i.month) + '-' + str(i.day) + '-' + str(i.day) + '-' + str(i.hour) + '-' + str(i.minute) + '-' + str(i.second)
            filenaam = 'media/' + "user" + str(now) + '.jpg'
            destination = open(filenaam, 'w+')
            main_pic = cv2.imwrite(filenaam, fram)
            destination.close()
            break
    # ending all processes
    cv2.destroyAllWindows()
    vs.stop()
    cap = Captured_Images(user_face_image = filenaam)
    cap.save()
    return redirect('home')






























    from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np

face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
classifier = load_model('EmotionDetectionModel.h5')

class_labels=['Angry','Happy','Neutral','Sad','Surprise']
path = r"DSC06030.jpg"
frame = cv2.imread(path)
gray = cv2.imread(path, 0)
# ret,frame=cap.read()
labels=[]
faces=face_classifier.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray=gray[y:y+h,x:x+w]
    roi_gray=cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)

    if np.sum([roi_gray])!=0:
        roi=roi_gray.astype('float')/255.0
        roi=img_to_array(roi)
        roi=np.expand_dims(roi,axis=0)

        preds=classifier.predict(roi)[0]
        label=class_labels[preds.argmax()]
        label_position=(x,y)
        cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
    else:
        cv2.putText(frame,'No Face Found',(20,20),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)


cv2.imwrite("test.jpg", frame)

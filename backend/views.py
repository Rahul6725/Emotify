from django.shortcuts import render, redirect
import numpy as np
import argparse, time, cv2, imutils, datetime, os
from imutils.video import VideoStream
from .models import Captured_Images

# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
    net = cv2.dnn.readNetFromCaffe("backend/deploy.prototxt.txt", "backend/res10_300x300_ssd_iter_140000.caffemodel")
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
            main_pic = cv2.imwrite(os.path.join(BASE_DIR, "static/images/user " + str(dt) + ".jpg"), fram)
            break
    # ending all processes
    cv2.destroyAllWindows()
    vs.stop()
    cap = Captured_Images(user_face_image = main_pic)
    cap.save()
    return redirect('home')

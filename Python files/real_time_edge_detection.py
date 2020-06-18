# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:24:56 2019

@author: user
"""

import cv2

face_data=r"D:\Datasets\data\haarcascades\haarcascade_frontalface_default.xml"
classifier = cv2.CascadeClassifier(face_data)
cap = cv2.VideoCapture(0)

ret = True

while ret :
    if cap.isOpened():
        ret,frame = cap.read()
        edges = cv2.Canny(frame,50,150)
        
        faces = classifier.detectMultiScale(frame)
        
        for x,y,w,h in faces :
            cv2.rectangle(edges , (x,y),(x+w,y+h),(255,255,255),10)
            
        cv2.imshow('video',edges)        
        if cv2.waitKey(30)==27:
            # escape key exit coz 27->escape
            break
    else :
        break
        
cv2.destroyAllWindows()
cap.release()
            
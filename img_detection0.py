# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:05:49 2019

@author: user
"""
  
import cv2
import numpy as np
from os import listdir
from os.path import isfile,join
import time

data_path = "D:\\ml\\data_images"
onlyfiles = []
for k in listdir(data_path):
    onlyfiles.append(k)


Training_Data , Labels = [] ,[]

for i , files in enumerate(onlyfiles):
    image_path = join(data_path, onlyfiles[i])
    images = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images,dtype=np.uint8))
    Labels.append(i)
    
Labels = np.asarray(Training_Data),np.asarray(Labels)

model = cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(Training_Data),np.asarray(Labels))

print('Model Training Completed ........')

face_classifier = cv2.CascadeClassifier(r"D:\Datasets\data\haarcascades\haarcascade_frontalface_default.xml")

def face_detector (img,size=0.5):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is() :
        return img,[]
    
    for (x,y,w,h) in faces :
        cv2.rectangle(img,(x,y),(x+w,y+h),2)
        roi = img[y:y+h , x:x+w]
        roi = cv2.resize(roi,(200,200))
        
    return img,roi

cap = cv2.VideoCapture(0)
while True :
    
    flag = False
    ret , frame = cap.read()
    
    image , face = face_detector(frame)
    
    try :
        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        result = model.predict(face)
        
        if result[1]<500:
            confidence  = int(100*(1-(result[1])/1000))
            display_string = str(confidence)+ '% Confidence it is user'
            cv2.putText(image , display_string,(10,10),cv2.FONT_HERSHLEY_COMPLEX,1,(250,120,255),2)
            
        if confidence > 80:
            
            cv2.putText(image,'Unlocked',(10,400),cv2.FONT_HERSHLEY_COMPLEX,2,(0,255,0),2)
            cv2.imshow('Face Cropper',image)
            cv2.waitKey(20)
            
        else :
            cv2.putText(image,'Locked',(10,400),cv2.FONT_HERSHLEY_COMPLEX,2,(0,0,255),2)
            cv2.imshow('Face Cropper',image)
            
    except :
        #cv2.putText(image,'Face not found',(10,400),cv2.FONT_HERSHLEY_COMPLEX,2,(255,0,0),2)
        cv2.imshow('Face Cropper',image)
        pass
    if cv2.waitkey(1)==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
#ser.close

     
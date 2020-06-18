# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 13:14:27 2019

@author: user
"""

import cv2

img = cv2.imread(r"C:\Users\user\Pictures\Saved Pictures\happy-person-11545688398rslqmyfw4g.png",0)
print(type(img))

face_cascade= cv2.CascadeClassifier(r"D:\Datasets\data\haarcascades\haarcascade_frontalface_default.xml")

re = cv2.resize(img, (int(img.shape[1]/4),int(img.shape[0]/4)))

faces = face_cascade.detectMultiScale(img)

for x,y,w,z in faces :
    cv2.rectangle(img , (x,y) , (x+w,y+z) , (0,255,255) , 3)

cv2.imshow('hi',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


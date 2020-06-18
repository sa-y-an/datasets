# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:50:45 2019

@author: shamaun
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread(r"C:\Users\shamaun\Desktop\Datasets\standard_test_images\standard_test_images\download.jpg")

face_data = r"C:\Users\shamaun\Desktop\Datasets\data\haarcascades\haarcascade_frontalface_alt.xml"
classifier = cv2.CascadeClassifier(face_data)

faces = classifier.detectMultiScale(img)

for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),
                  (x+w,y+h),
                  (255,0,0),2)


cv2.imshow('lena',img)
cv2.waitKey(0)
cv2.destroyAllWindows()




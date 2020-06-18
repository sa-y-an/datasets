# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 09:47:22 2019

@author: shamaun
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"C:\Users\shamaun\Desktop\Datasets\standard_test_images\standard_test_images\lena_color_512.tif")


#how to convert BGR to GRAY

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img,100,250)

canvas = np.zeros_like(img)
#drawing shapes

cv2.rectangle(canvas,(100,100),(200,200),
              (255,0,255),-5)
cv2.circle(canvas,(100,100),100,(255,255,255),
           -5)
cv2.line(canvas,(200,200),(300,300),
         (0,0,255),10)
text = "hello"
cv2.putText(canvas,text,(300,300),cv2.FONT_HERSHEY_PLAIN,
            5,(255,0,0),1)

cv2.imshow('lena',canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()





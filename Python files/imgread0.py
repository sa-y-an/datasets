# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:19:56 2019

@author: user
"""

import cv2
# reads images as BGR
import matplotlib.pyplot as plt
# reads as RGB
import numpy as np

img = cv2.imread(r"D:\Datasets\standard_test_images\standard_test_images\lena_color_512.tif")

plt.imshow(img)
plt.show()

# conversion from BGR to RGB

#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



# this changes the color of the array
# this causes cv2 to show different color 

# plotting the image
plt.imshow(img)
plt.show()

# displaying the image

cv2.imshow('hello',img)
cv2.waitKey(0)  # wait for 0 miliseconds
cv2.destroyAllWindows() # destroy all windows

#always run all three together else kernal runs in infinite loop

# coversion from rgb to grey

# finding edges in  the edges

edges = cv2.Canny(img,100,150)
'''
cv2.imshow('hello',edges)
cv2.waitKey(0)  # wait for 0 miliseconds
cv2.destroyAllWindows() # destroy all windows
'''
canvas = np.zeros_like(img)
# this creates a black color background
# since 

# drawing shapes on images

cv2.rectangle(canvas,(100,100),(200,200),(255,255,255),-5) # takes 
# arguments where 
# - values in size gives filled shapes

cv2.circle(canvas,(100,100),100,(255,0,255),5)
cv2.line(canvas,(200,200),(300,300),(0,0,255),5)
text = 'hello world'

cv2.putText(canvas,text,(300,300),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
cv2.imshow('hello',canvas)
cv2.waitKey(0)  # wait for 0 miliseconds
cv2.destroyAllWindows() # destroy all windows

# line detection 







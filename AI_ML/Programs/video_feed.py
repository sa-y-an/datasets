# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:24:26 2019

@author: shamaun
"""
import cv2
cap = cv2.VideoCapture(r"C:\Users\shamaun\Desktop\Datasets\test2.mp4")

ret=True
while ret:
    if cap.isOpened:
        ret,frame=cap.read()
    else:
        break

        
    cv2.imshow('video',frame)
    if cv2.waitKey(30)==27:
        break

cv2.destroyAllWindows()
cap.release()

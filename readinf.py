# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:11:29 2019

@author: user
"""

import cv2

cap = cv2.VideoCapture(0)
# video from camera attached to the system
# according to port we can change the bios port cv2.VideoCapture(1)
# if we want to take from a file place the file name in the ()


# reading from camera

ret = True

while ret :
    
    if cap.isOpened():
        ret , frame = cap.read()
        cv2.imshow('video',frame)
        edges  = cv
        if cv2.waitKey(30)==27 :
            break 
    else :
        break
cv2.destroyAllWindows()
cap.release()
            

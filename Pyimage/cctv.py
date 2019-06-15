# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:16:49 2019

@author: sandeepv
"""

import cv2
cap = cv2.VideoCapture("rtsp://admin:ADMIN1234@192.168.225.38:554/cam/realmonitor?channel=5&subtype=0")

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

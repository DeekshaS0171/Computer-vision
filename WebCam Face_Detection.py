# -*- coding: utf-8 -*-
#FACE DETECTION

import numpy as np
import cv2

Initial_frame = None
#temp_image = cv2.imread('C:/Users/deeks/Desktop/Adsoft/CV/CV_Projects/20190402_120736.jpg',1)
#resize_img = cv2.resize(temp_image,(int(temp_image.shape[0]/14),int(temp_image.shape[1]/6)))

Cam = cv2.VideoCapture(0)

while(True):
    ret,frame = Cam.read()
    gray_Image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_temp = cv2.cvtColor(resize_img,cv2.COLOR_BGR2GRAY)
        
    
    features = cv2.CascadeClassifier('C:/Users/deeks/Desktop/Adsoft/CV/Module_1_Face_Recognition/haarcascade_frontalface_default.xml')
    Detect_Face = features.detectMultiScale(gray_Image,scaleFactor = 1.05, minNeighbors = 5, minSize = (40,40))
    for (x,y,w,h) in Detect_Face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)# x+w and y+h are to limit the rectangle area
        text = 'Face Detected'
        cv2.putText(frame,text,(10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    cv2.imshow("Face",frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
Cam.release()
cv2.destroyAllWindows()

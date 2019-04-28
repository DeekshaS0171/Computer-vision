# -*- coding: utf-8 -*-



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
    #Noise reduction
    gray_frame = cv2.GaussianBlur(gray_Image,(5,5),1)
    
    if Initial_frame is None:
        Initial_frame = gray_frame
        continue
        
    diff = cv2.absdiff(Initial_frame,gray_frame)
    
    #Let's threshold the image so that we can get binary mage to fine contours to use as boundaries
    
    retu,thresh = cv2.threshold(diff,30,255,cv2.THRESH_BINARY)
    image,contour,heirarcy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for c in contour:
        if cv2.contourArea(c) >10000:
           x,y,w,h = cv2.boundingRect(c)
           cv2.rectangle(frame,(x,y),(x+w , y+h),(0,255,0),3)
           text = "motion detected"
           cv2.putText(frame,text,(10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            
    cv2.imshow("Motion Detection",frame)    
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
Cam.release()
cv2.destroyAllWindows()
        
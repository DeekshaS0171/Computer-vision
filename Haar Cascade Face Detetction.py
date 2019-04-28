# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:30:55 2019

@author: deeks
"""

#####
#Face Detection  using haar cascading.

import cv2
import numpy as np

faces = cv2.imread("C:\\Users\\deeks\\Desktop\\Adsoft\CV\\Ex_Files_OpenCV_Python_Dev\\Exercise Files\\Ch04\\04_05 Begin\\faces.jpeg",1)
gray = cv2.cvtColor(faces,cv2.COLOR_BGR2GRAY)

Cascade_faces = cv2.CascadeClassifier("C:\\Users\\deeks\\Desktop\\Adsoft\\CV\\Ex_Files_OpenCV_Python_Dev\\Exercise Files\\Ch04\\04_05 Begin\\haarcascade_frontalface_default.xml")

Detect_Face = Cascade_faces.detectMultiScale(gray,scaleFactor = 1.05, minNeighbors = 5, minSize = (40,40))
#This returs a list of locations where the faces were detected
#scaleFactor is the compensating factor for the faces closer to the camera.
#minNeighbors =sets the number of nearby objects xdetects required before considering as a face
#minSize = if the face is of atleast (40,40 )size


print(len(Detect_Face))

for (x,y,w,h) in Detect_Face:
    cv2.rectangle(faces,(x,y),(x+w,y+h),(0,255,0),3)# x+w and y+h are to limit the rectangle area

cv2.imshow("Detected faces",faces)
cv2.waitKey()
cv2.destroyAllWindows()



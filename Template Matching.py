# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:26:06 2019

@author: deeks
"""

################################################
#Template Matching

import cv2
import numpy as np

Image = cv2.imread("C:\\Users\\deeks\\Desktop\\Adsoft\\CV\\Ex_Files_OpenCV_Python_Dev\\Exercise Files\\Ch04\\04_03 Begin\\players.jpg",1)#0
template = cv2.imread("C:\\Users\\deeks\\Desktop\\Adsoft\\CV\\Ex_Files_OpenCV_Python_Dev\\Exercise Files\\Ch04\\04_03 Begin\\template.jpg",1)#0
Image_copy = Image.copy()
print("Image Shape :{0}\nTemplate Shape:{1}".format(Image.shape,template.shape))

gray_Image = cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
gray_template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)

Temp_match = cv2.matchTemplate(gray_Image,gray_template,cv2.TM_CCOEFF_NORMED)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(Temp_match)

cv2.circle(Temp_match,max_loc,25,255,3)
cv2.circle(Image_copy,max_loc,25,(0,255,0),3)

print(min_val,max_val,min_loc,max_loc)


cv2.imshow("Original Image",Image)
cv2.imshow("Template",template)
cv2.imshow("GrayScaled Image", gray_Image)
cv2.imshow("GrayScaled Template",gray_template)
cv2.imshow("Template Matched",Temp_match)
cv2.imshow("Template Matched Original Image",Image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()


### While Template matching, the color of the objects doesn't matter much so in order to reduce the time of computation, it is better to use gray scale
# Not a perfect match as the size of the template and the object in the image are different


'''
Created on Sep 9, 2017

@author: inayat
'''

# import the required  packages
#from imutils.video import WebcamVideoStream
#from imutils.video import FPS
import numpy as np
import argparse
#import imutils
import time
import cv2

#from utils.fps2 import FPS2

import dlib

from trackers.camshifttracker import CAMShiftTracker


WebCam = cv2.VideoCapture(0).start()
time.sleep(1.0)
    
    
    # initialize dlib face detector
    
frontFaceDetector = dlib.get_frontal_face_detector() 
    
    
    # camShift tracker
    
camShifTracker = None
    
currentWindow = None
    
    
boolDetectFaceinfirsFrameOnly = True
    
    
    
    # loop over the frames obtained from the webcam
while True:
     
        frame1 = WebCam.read()
        frame = cv2.flip(frame1,1)
        
        if boolDetectFaceinfirsFrameOnly:
            
            faceRect = frontFaceDetector(frame, 0)
            
            if(not len(faceRect) ):
                print("[info] Face not found")
                continue
            
            
            
            
            bbox = faceRect[0]
            
                        
            # convert dlib rect to opencv rect
            
            currentWindow = (int(bbox.left()), int(bbox.top()), int(bbox.right() - bbox.left()),
                         int(bbox.bottom() - bbox.top()) )
            
            # intialize the CAMShift Tracker
            camShifTracker = CAMShiftTracker(currentWindow, frame)
            
            boolDetectFaceinfirsFrameOnly = False
            continue 
        
        
            
        
        camShifTracker.computeNewWindow(frame)
        
        x,y, w, h = camShifTracker.getCurWindow()
        
        bkprojectImage = camShifTracker.getBackProjectedImage(frame)
        
        cv2.imshow("CAMShift Face in Back Project Image", bkprojectImage)
        
        
        
        # display the current window 
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2, cv2.LINE_AA)
        
        
        rotatedWindow = camShifTracker.getRotatedWindow()
        #display rotated window
        cv2.polylines(frame, [rotatedWindow], True, (0,255,0), 2, cv2.LINE_AA)
           
        cv2.putText(frame, "Tracking",
                    (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        
        # show the frame and update the FPS counter
        cv2.imshow("CAMShift Face Tracking", frame)
        
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break
    # do a bit of cleanup
cv2.destroyAllWindows()
WebCam.stop()

#ARIS_Tracker.py
#Created by Chris Rillahan
#Last Updated: 12/29/2015
#Written with Python 2.7.11, OpenCV 3.0

#This script simply plays back an ARIS file at present. The ARIS data has been
#exported as a *.mp4 file.

import numpy as np
import cv2

#Set the path and file location
path = "C:\\Users\\User\\OneDrive\\ARIS\\ARIS_Tracker\\2015-06-03_023000.mp4"
print(path)

#Load the video
video = cv2.VideoCapture(path)
#print(video.isOpened())

#Setup the background subtraction masks
fgbg = cv2.createBackgroundSubtractorMOG2(history = 25, varThreshold = 60,
                detectShadows = False)
fgbgKK = cv2.createBackgroundSubtractorKNN(history = 25, dist2Threshold = 20.0,
                detectShadows = False)

#Create the window and start the loop.
cv2.namedWindow('Video', flags = cv2.WINDOW_NORMAL)
cv2.namedWindow('MOG', flags = cv2.WINDOW_NORMAL)
cv2.namedWindow('KNN', flags = cv2.WINDOW_NORMAL)

success = True
while success == True:
    success, image = video.read()
    FPS = video.get(cv2.CAP_PROP_FPS)

    fgmask = fgbg.apply(image)
    knnmask = fgbg.apply(image)
    
    cv2.imshow('Video', image)
    cv2.imshow('MOG', fgmask)
    cv2.imshow('KNN', knnmask)
#    cv2.waitKey(int(FPS/60*1000)) #Actual Playback Speed
    k = cv2.waitKey(10)
    if k == 27:
            video.release()
            break
    
cv2.destroyAllWindows()

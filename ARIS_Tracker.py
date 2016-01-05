#ARIS_Tracker.py
#Created by Chris Rillahan
#Last Updated: 12/29/2015
#Written with Python 2.7.11, OpenCV 3.0

#This script simply plays back an ARIS file at present. The ARIS data has been
#exported as a *.mp4 file.

#To-do
#   Convert everything to greyscale.

import numpy as np
import cv2

#Set the path and file location
path = "C:\\Users\\User\\OneDrive\\ARIS\\ARIS_Tracker\\2015-06-03_023000.mp4"
print(path)

#Load the video
video = cv2.VideoCapture(path)
#print(video.isOpened())
_, avg = video.read()
avg1 = cv2.cvtColor(avg, cv2.COLOR_BGR2GRAY)
avg2 = np.float32(avg1)


kernel = np.ones((3,3), np.uint8)

#Create the window and start the loop.
cv2.namedWindow('Video', flags = cv2.WINDOW_NORMAL)
#cv2.namedWindow('KNN', flags = cv2.WINDOW_NORMAL)
cv2.namedWindow('Ave', flags = cv2.WINDOW_NORMAL)

success = True
while success == True:
    success, image = video.read()
    bwimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    FPS = video.get(cv2.CAP_PROP_FPS)
    
    cv2.accumulateWeighted(bwimage, avg2, 0.01)
    res1 = cv2.convertScaleAbs(avg1)
    fg = cv2.subtract(bwimage, res1)
    
    #fg2 = cv2.medianBlur(fg, 5)
    fg3 = cv2.add(fg, fg)
    _,thr = cv2.threshold(fg3, 20, 254, cv2.THRESH_BINARY)
    morphEx = cv2.morphologyEx(thr, cv2.MORPH_OPEN, kernel)
    morphEx2 = cv2.morphologyEx(morphEx, cv2.MORPH_CLOSE, kernel)

    cimg,contours0, hier = cv2.findContours(morphEx2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print 'new'
    print contours0
    contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours0]
    contours1 = [cv2.contourArea(cnt) for cnt in contours0]
    #print contours
    print contours1
    #filt_cont = 
    cv2.drawContours(image, contours0, -1, (128,255,255), 3)

    #run through contour areas to filter out small contours.
    
    cv2.imshow('Video', image)
    #cv2.imshow('KNN', thr)
    cv2.imshow('Ave', morphEx2)
#    cv2.waitKey(int(FPS/60*1000)) #Actual Playback Speed
    k = cv2.waitKey(10)
    if k == 27:
            video.release()
            break
    
cv2.destroyAllWindows()

# Chris Rillahan
#ARIS Tracker

import cv2

path = "C:\\Users\\User\\OneDrive\\ARIS\\ARIS_Tracker\\2015-06-03_023000.mp4"
print(path)

video = cv2.VideoCapture(path)
cv2.namedWindow('Video', flags = cv2.WINDOW_NORMAL)
#print(video.isOpened())

success = True


while success == True:
    success, image = video.read()
    FPS = video.get(cv2.CAP_PROP_FPS)
    cv2.imshow('Video', image)
#    cv2.waitKey(int(FPS/60*1000)) #Actual Playback Speed
    k = cv2.waitKey(10)
    if k == 27:
            break
            video.release()
            cv2.destroyAllWindows()
    
cv2.destroyAllWindows()

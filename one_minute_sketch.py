import cv2
import random
import pafy

#This script as of right now only captures a random frame out of a downloaded video.
#I will be creating an app that can take a video from youtube that shows a random frame for a minute.
#Intended for electronic music videos

vidcap = cv2.VideoCapture('video.mp4')
# get total number of frames
totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
randomFrameNumber=random.randint(0, totalFrames)
# set frame position
vidcap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
success, image = vidcap.read()
if success:
    cv2.imwrite("random_frame.jpg", image)
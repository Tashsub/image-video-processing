import cv2

#if this was a video/mp4 file being passed then speify the path here
#otherwise 0 for the camera
video=cv2.VideoCapture(0)

video.release()
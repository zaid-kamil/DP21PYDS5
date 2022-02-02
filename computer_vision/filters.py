import cv2
import numpy as np
from cv2 import VideoCapture

cap = VideoCapture(0)

while True:
    status,frame = cap.read()
    if not status:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2YCrCb)
    cv2.imshow('window',frame)
    cv2.imshow('gray',gray)
    merged = np.hstack((frame,rgb))
    cv2.imshow("merged",merged)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()


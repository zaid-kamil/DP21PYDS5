# pip install opencv-contrib-python
import cv2

img = cv2.imread("D:/Users/HP 346 G3/OneDrive/Pictures/pika.png")
print("the image has",img.size,"pixels")
cv2.imshow("output",img)
# cv2.imshow('output2',img*2)
cv2.imshow('output3',img/2)
# cv2.imshow('output4',img**12)
cv2.waitKey(0) # K is capital here
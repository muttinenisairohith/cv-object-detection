import cv2
import numpy as np
img= cv2.imread('opencvobject.jpeg',1)
# Convert BGR to HSV
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.namedWindow('hsv', cv2.WINDOW_NORMAL)
cv2.namedWindow('res', cv2.WINDOW_NORMAL)
cv2.namedWindow('mask', cv2.WINDOW_NORMAL)

cv2.imshow('image',img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
blue=np.uint8([[[255,0,0]]])
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
print hsv_blue
# define range of blue color in HSV
lower_blue = np.array([100,0,0])
upper_blue = np.array([103,255,255])
# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)
# Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)
cv2.imshow('mask',mask)
cv2.imshow('hsv',hsv)
cv2.imshow('res',res)
k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()


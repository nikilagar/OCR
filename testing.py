import numpy as np
import cv2
import thinnigSkeletonization as tsk
img=cv2.imread("images/fuckingImage.jpg",cv2.IMREAD_GRAYSCALE);
img=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
img=tsk.getSkeletonizedImage(img)
cv2.imshow("JJE",img)
cv2.waitKey()
#tsk.getSkeletonizedImage(arr)
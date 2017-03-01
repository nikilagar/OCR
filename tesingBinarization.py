import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('images/thresh_2.png',0)
#img = cv2.medianBlur(img,3)

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY,11,2)
cv2.imshow("HII",th3)
cv2.waitKey()

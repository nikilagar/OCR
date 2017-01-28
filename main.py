import cv2
from BinarizeImage import *
from matplotlib import pyplot as py
import componentGetter

image=cv2.imread("images/test.jpg",0)
image=getBinarizedImage(image)
components=componentGetter.getComponents(image)
print(len(components))
#print(components)



py.imshow(image,'gray')
py.show()
print(image)

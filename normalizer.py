import cv2
import thinnigSkeletonization as tsk
import BinarizeImage as BI
import numpy as np

expectedHeight=24
def getNormalizedImage(img):
    global expectedHeight
    newAspectRatio=1.0*expectedHeight/len(img)
    img=cv2.resize(img,(0,0),fx=newAspectRatio,fy=newAspectRatio)
    if(len(img[0])<24):
        dif=(24-len(img[0]))/2
        img=cv2.copyMakeBorder(img,0,0,int(dif),24-int(dif)-len(img[0]),cv2.BORDER_CONSTANT,value=255)
    elif(len(img[0])>24):
        img=cv2.resize(img,(24,24))
    img=BI.getBinarizedImage(img)
    return tsk.getSkeletonizedImage(img)



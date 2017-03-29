import cv2
import thinnigSkeletonization as tsk
import BinarizeImage as BI
import numpy as np

expectedHeight=22
def getNormalizedImage(img):
    global expectedHeight
    newAspectRatio=1.0*expectedHeight/len(img)
    img=cv2.resize(img,(0,0),fx=newAspectRatio,fy=newAspectRatio)
    if(len(img[0])<expectedHeight):
        dif=(expectedHeight-len(img[0]))/2
        img=cv2.copyMakeBorder(img,0,0,int(dif),expectedHeight-int(dif)-len(img[0]),cv2.BORDER_CONSTANT,value=255)
    elif(len(img[0])>expectedHeight):
        img=cv2.resize(img,(expectedHeight,expectedHeight))
    img=BI.getBinarizedImage(img)
    return tsk.getSkeletonizedImage(img)



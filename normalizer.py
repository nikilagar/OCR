import cv2
import thinnigSkeletonization as tsk
import BinarizeImage as BI
expectedHeight=36
def getNormalizedImage(img):
    global expectedHeight
    newAspectRatio=1.0*expectedHeight/len(img[0])
    img=cv2.resize(img,(0,0),fx=newAspectRatio,fy=newAspectRatio)
    img=BI.getBinarizedImage(img)
    return tsk.getSkeletonizedImage(img)



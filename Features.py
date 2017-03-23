import normalizer
import cv2
import thinnigSkeletonization as tsk
import BinarizeImage as bi

#calculating perimeters
def getPerimeter(img):
    x,y=len(img),len(img[0])
    cnt=0
    for i in range(x):
        for j in range(y):
            if(img[i][j]==0):
                cnt+=1
    return cnt


#Dividing into 4 zones upper-left, upper-right, lower-left and lower-right
def getZonesValue(img):
    x,y=int(len(img)),int(len(img[0]))
    midx,midy=int(x/2),int(y/2)
    zone=[0,0,0,0]
    for i in range(x):
        for j in range(y):
            if(img[i][j]==0):
                if(i<midx):
                    if(j<midy):
                        zone[0]+=1
                    else:
                        zone[1]+=1
                else:
                    if(j<midy):
                        zone[2]+=1
                    else:
                        zone[3]+=1
    return zone
#Calculating moment about bottomline middle point
def getMoment(img):
    c=1


#Returning list of features
def getFeatures(img):
    featureList=[]
    cv2.imshow("char",img)
    cv2.waitKey()
    img=normalizer.getNormalizedImage(img)
    zones=getZonesValue(img)
    for i in zones:
        featureList.append(i)
    return featureList

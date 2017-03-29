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

def getEndPoints(img) :
    y,x = int(len(img)), int(len(img[0]))
    midx = x/2
    midy = y/2
    dx=[0,1,1,1,0,-1,-1,-1]
    dy=[-1,-1,0,1,1,1,0,-1]
    inter1,inter2,inter3,inter4=0,0,0,0
    open1,open2,open3,open4=0,0,0,0
    print (x,y)
    for i in range(y) :
        for j in range(x) :
            c=0
            for k in range(8) :
                if(i+dy[k]>=0 and i+dy[k]<y and j+dx[k]>=0 and j+dx[k]<x ) :
                    #print(i + dy[k], j + dx[k])
                    if(img[i+dy[k]][j+dx[k]]==0) :

                        c+=1
            if(i<midy and j<midx) :
                if(c==1) :
                    open1+=1
                elif(c>2) :
                    inter1+=1
            elif(i<midy and j>midx) :
                if(c==1) :
                    open2+=1
                elif(c>2) :
                    inter2+=1
            elif(i>midy and j<midx) :
                if(c==1) :
                    open3+=1
                elif(c>2) :
                    inter3+=1
            elif(i>midy and j>midx) :
                if(c==1) :
                    open4+=1
                elif(c>2) :
                    inter4+=1

    op,ii = [],[]
    '''
    if (open1>0) :
        for i in range(y) :
            for j in range(x) :
                print (img[i][j],end=" ")
            print ("")
        cv2.waitKey()
    '''
    op.extend((open1,open2,open3,open4))
    ii.extend((inter1,inter2,inter3,inter4))
    op = op + ii
    return op



#Returning list of features
def getFeatures(img):
    featureList=[]
    img=normalizer.getNormalizedImage(img)
    intersections = getCrossing(img)
    for i in intersections :
        featureList.append(i)
    '''
    zones=getZonesValue(img)
    for i in zones:
        featureList.append(i)
    '''
    return featureList


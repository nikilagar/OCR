import numpy as np
import cv2
dx=np.array([0,0,-1,-1,0,1,1,1,0,-1])
dy=np.array([0,0,0,1,1,1,0,-1,-1,-1])
p=np.zeros((11))
def convertToZeroOrOne(point):
    return point==0
def subIteration(img,type):
    x,y=img.shape
    global dx,dy,retMatr,p
    stack=[]
    for i in range(1,x-1):
        for j in range(1,y-1):
            canBeDeleted=True
            B=0
            for k in range(1,10):
                p[k]=convertToZeroOrOne(img[i+dx[k]][j+dy[k]])
                B+=p[k]
            p[10]=p[2]
            B-=p[1]
            Acnt=0
            for k in range(2,10):
                if p[k]==0 and p[k+1]==1:
                    Acnt+=1
            if(B<2 or B>6 or Acnt!=1):
                canBeDeleted=False
            if type==0 :
                if (p[2]*p[4]*p[6]!=0 or p[4]*p[6]*p[8]!=0) :
                    canBeDeleted=False
            else :
                if (p[2]*p[4]*p[8]!=0 or p[2]*p[6]*p[8]!=0) :
                    canBeDeleted=False
            if img[i][j]==0 and canBeDeleted==True:
                stack.append([i,j])
    while len(stack)!=0 :
         lastInd=len(stack)-1
         x,y=stack[lastInd][0],stack[lastInd][1]
         img[x][y]=255
         stack.pop()
    return img

def frameImage(img):
    x, y = img.shape
    img2 = np.zeros((x + 2, y +2))  #increasing size of image by +2 x , +2 y
    for i in range(0, x+2):
        for j in range(0, y+2):
            if(i==0 or i==x+1 or j==0 or j==y+1):
                img2[i][j]=255
            else :
                img2[i][j] = img[i - 1][j - 1]
    return img2

def getSkeletonizedImage(img):
    img=frameImage(img) #frame image into a grid of ones :0
    while True:
        temImg=img.copy()
        img=subIteration(img,0) #subIteration first
        img=subIteration(img,1) #subIteration second
        if np.array_equal(temImg,img):
            break
    return img
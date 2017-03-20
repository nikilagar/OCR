import cv2
import classifier
#further refining upper And Lower bound of character
def refine(img,pts):
    x1,y1,x2,y2=pts[0],pts[1],pts[2],pts[3]
    minx1=x2
    maxx2=x1
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if(img[i][j]==0):
                minx1=min(minx1,i)
                maxx2=max(maxx2,i)
    return [minx1,y1,maxx2,y2]
def getVerticalCount(img,x1,x2,y):
    cnt=0
    for i in range(x1,x2+1):
        if img[i][y]==0:
            cnt+=1
    return cnt
def segment(img,lines):
    imgy=len(img[0])
    characterBounds=[]
    for curLine in lines:
        y=0
        while(y<imgy):
            f=False
            vtCnt=getVerticalCount(img,curLine[0],curLine[1],y)
            if vtCnt>0:
                f=True
                pr=y
            while y<imgy and vtCnt>0:
                y+=1
                if(y<imgy):
                    vtCnt=getVerticalCount(img,curLine[0],curLine[1],y)
            if(f==True):
                y-=1
                characterBounds.append(refine(img,[curLine[0],pr,curLine[1],y]))
            y+=1
    return  characterBounds


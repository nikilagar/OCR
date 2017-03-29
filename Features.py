import normalizer
import cv2
import thinnigSkeletonization as tsk
import BinarizeImage as bi
import math
import numpy as np
from scipy import signal

'''
Image is considered to be a matrix of 0 and 255
0 is for black and 255 for white
x and y are accessed in this way
    y ---------
 x   ..........
 |   ..........
 |   ..........
 |   ..........
 |   ..........

'''
#calculating perimeters
def getPerimeter(img):
    x, y = len(img), len(img[0])
    cnt = 0
    for i in range(x):
        for j in range(y):
            if (img[i][j] == 0):
                cnt += 1
    return cnt

#Wavelet transform
def waveletTransform(img):
    imgArray = np.array(img)
    cwtmatr = signal.cwt(img, signal.ricker, np.range(1,25))
    return cwtmatr


def getFourierTransformvalues(img):
    imgArray = np.asarray(img)
    a = np.fft.fft2(imgArray)
    return a

############Walsh Hadamard Transform ##############
def bit_reverse_traverse(a):
    # (c) 2014 Ryan Compton
    # ryancompton.net/2014/06/05/bit-reversal-permutation-in-python/
    n = a.shape[0]
    assert (not n & (n - 1))  # assert that n is a power of 2
    if n == 1:
        yield a[0]
    else:
        even_index = np.arange(n / 2) * 2
        odd_index = np.arange(n / 2) * 2 + 1
        for even in bit_reverse_traverse(a[even_index]):
            yield even
        for odd in bit_reverse_traverse(a[odd_index]):
            yield odd


def get_bit_reversed_list(l):
    # (c) 2014 Ryan Compton
    # ryancompton.net/2014/06/05/bit-reversal-permutation-in-python/
    n = len(l)
    indexs = np.arange(n)
    b = []
    for i in bit_reverse_traverse(indexs):
        b.append(l[i])
    return b

#Return list of end points and intersection points in four quadrants
def getEndPointsNIntersectionPoints(img) :
    y,x = int(len(img)), int(len(img[0]))
    midx = x/2
    midy = y/2
    dx=[0,1,1,1,0,-1,-1,-1]
    dy=[-1,-1,0,1,1,1,0,-1]
    inter1,inter2,inter3,inter4=0,0,0,0
    open1,open2,open3,open4=0,0,0,0
    for i in range(y) :
        for j in range(x) :
            c=0
            if(img[i][j]!=0) :
                continue
            for k in range(8) :
                if(i+dy[k]>=0 and i+dy[k]<y and j+dx[k]>=0 and j+dx[k]<x ) :
                    #print(i + dy[k], j + dx[k])
                    if(img[i+dy[k]][j+dx[k]]==0) :

                        c+=1
            if(i<midy and j<midx) :
                if(c==1) :
                    open1+=1
                elif(c>3) :
                    inter1+=1
            elif(i<midy and j>midx) :
                if(c==1) :
                    open2+=1
                elif(c>3) :
                    inter2+=1
            elif(i>midy and j<midx) :
                if(c==1) :
                    open3+=1
                elif(c>3) :
                    inter3+=1
            elif(i>midy and j>midx) :
                if(c==1) :
                    open4+=1
                elif(c>3) :
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



#Dividing into 4 zones upper-left, upper-right, lower-left and lower-right
def getZonesValue(img):
    x, y = int(len(img)), int(len(img[0]))
    midx, midy = int(x / 2), int(y / 2)
    zone = [0, 0, 0, 0]
    for i in range(x):
        for j in range(y):
            if (img[i][j] == 0):
                if (i < midx):
                    if (j < midy):
                        zone[0] += 1
                    else:
                        zone[1] += 1
                else:
                    if (j < midy):
                        zone[2] += 1
                    else:
                        zone[3] += 1
    return zone


#Calculating moment about Origin
def getMoment(img):
    moment = [0.0 for i in range(0,5)]
    m0x,m0y=len(img)/2,len(img[0])/2
    m1x,m1y=0,0
    m2x,m2y=0,len(img[0])-1
    m3x,m3y=len(img)-1,len(img[0])-1
    m4x,m4y=len(img)-1,0
    for i in range(0, len(img)):
        for j in range(0, len(img[0])):
            if (img[i][j] == 0):
                if(i!=m0x and j!=m0y):
                    moment[0] += math.cos(math.atan(abs(i - m0x) * 1.0 / abs(j - m0y))) * math.sqrt(
                        abs(i - m0x) * abs(i - m0x) + abs(j - m0y) * abs(j - m0y))
                if (i != m1x and j != m1y):
                    moment[1] += math.cos(math.atan(i * 1.0 / j)) * math.sqrt(i * i + j * j)
                if (i != m2x and j != m2y):
                    moment[2] += math.cos(math.atan(abs(i - m2x) * 1.0 / abs(j - m2y))) * math.sqrt(
                        abs(i - m2x) * abs(i - m2x) + abs(j - m2y) * abs(j - m2y))
                if (i != m3x and j != m3y):
                    moment[3] += math.cos(math.atan(abs(i - m3x) * 1.0 / abs(j - m3y))) * math.sqrt(
                        abs(i - m3x) * abs(i - m3x) + abs(j - m3y) * abs(j - m3y))
                if (i != m4x and j != m4y):
                    moment[4] += math.cos(math.atan(abs(i - m4x) * 1.0 / abs(j - m4y))) * math.sqrt(
                        abs(i - m4x) * abs(i - m4x) + abs(j - m4y) * abs(j - m4y))
    return moment


#Return Crossings along 2 diagonals and n + m lines horizontal and verticals
def crossings(img):
    lenx, leny = len(img), len(img[0])
    cros = [ 0 for i in range(0,lenx+leny+2) ]
    j = 0
    state = 1
    for i in range(0, lenx):
        if (img[i][j] == 0 and state == 1):
            cros[0] += 1
            state = 0
        elif img[i][j] == 255 and state == 0:
            cros[0] += 1
            state = 1
        j += 1
    j = 0
    state = 1
    for i in range(lenx - 1, -1, -1):
        if (img[i][j] == 0 and state == 1):
            cros[1] += 1
            state = 0
        elif img[i][j] == 255 and state == 0:
            cros[1] += 1
            state = 1
        j += 1
    for i in range(0, lenx):
        state=1
        for j in range(0,leny):
            if (img[i][j] == 0 and state == 1):
                cros[i+2] += 1
                state = 0
            elif img[i][j] == 255 and state == 0:
                cros[i+2] += 1
                state = 1
    for j in range(0, leny):
        state = 1
        for i in range(0,lenx):
            if (img[i][j] == 0 and state == 1):
                cros[2+lenx+j] += 1
                state = 0
            elif img[i][j] == 255 and state == 0:
                cros[2+lenx+j] += 1
                state = 1

    return cros



#Returning list of features
def getFeatures(img):
    featureList = []
#    cv2.imshow("SEEM ME Before nomralization", img)
    img = normalizer.getNormalizedImage(img)
#    cv2.imshow("SEEM ME AFTER nomralization",img)
#    cv2.waitKey()
    zones = getZonesValue(img)

    for i in zones:
        featureList.append(i)
    featureList += crossings(img)
    featureList += (getMoment(img))
    featureList += getEndPointsNIntersectionPoints(img)
#    featureList+=getFourierTransformvalues(img).tolist()

    return featureList

'''    for i in img:
        x = get_bit_reversed_list(i)
        featureList+=x
#    wavelet = waveletTransform(img)
    featureList+=wavelet
'''

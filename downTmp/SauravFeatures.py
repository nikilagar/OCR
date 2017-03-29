import normalizer
import cv2
import thinnigSkeletonization as tsk
import BinarizeImage as bi
import math
import numpy as np
from scipy.fftpack import fftfreq, fftshift
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
    moment = 0.0
    for i in range(0, len(img)):
        for j in range(0, len(img[0])):
            if (img[i][j] == 0):
                moment += math.cos(math.atan(i * 1.0 / j)) * math.sqrt(i * i + j * j)
    return moment



def crossings(img):
    cros = [0, 0, 0, 0]
    lenx, leny = len(img), len(img[0])
    state = 1
    for i in range(0, lenx):
        j = int(leny / 2)
        if (img[i][j] == 0 and state == 1):
            cros[0] += 1
            state = 0
        elif img[i][j] == 255 and state == 0:
            cros[0] += 1
            state = 1
    state = 1
    for j in range(0, leny):
        i = int(lenx / 2)
        if (img[i][j] == 0 and state == 1):
            cros[1] += 1
            state = 0
        elif img[i][j] == 255 and state == 0:
            cros[1] += 1
            state = 1
    j = 0
    state = 1
    for i in range(0, lenx):
        if (img[i][j] == 0 and state == 1):
            cros[2] += 1
            state = 0
        elif img[i][j] == 255 and state == 0:
            cros[2] += 1
            state = 1
        j += 1
    j = 0
    state = 1
    for i in range(lenx - 1, -1, -1):
        if (img[i][j] == 0 and state == 1):
            cros[3] += 1
            state = 0
        elif img[i][j] == 255 and state == 0:
            cros[3] += 1
            state = 1
        j += 1
    return cros

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
#################wavelet transform###############
def waveletTransform(img):
    imgArray = np.array(img)
    cwtmatr = signal.cwt(img, signal.ricker, np.range(1,25))
    return cwtmatr 

#Returning list of features
def getFeatures(img):
    featureList = []
    cv2.imshow("Before ",img)
    img = normalizer.getNormalizedImage(img)
    #cv2.imshow("SEEM ME AFTER nomralization",img)
    #cv2.waitKey()
    zones = getZonesValue(img)
    #fourierT = getFourierTransformvalues(img)
    #print(fourierT)
 
    wavelet = waveletTransform(img)

    for i in zones:
        featureList.append(i)
    featureList += crossings(img)
    featureList.append(getMoment(img))

   # for i in fourierT:
    #    featureList.append(i)
    for i in img:
        x = get_bit_reversed_list(i)
        for j in x:
            featureList.append(j)

    for i in wavelet:
        featureList.append(i)

    return featureList

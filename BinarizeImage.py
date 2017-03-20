import cv2
import numpy as np


def getBinarizedImage(img):
#    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) #reading image in grayscale  format :P

    #kernel=np.ones((5,5),np.uint8)
    #img_erosion=cv2.erode(img,kernel,iterations=1)
    #img_dilation=cv2.dilate(img_erosion,kernel,iterations=1)

    binarizedImage=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) #Applying gauss Meth to bin ;P
    #binarizedImage = cv2.medianBlur(img, 3) #reducing noise (taking mean of 7X7 grid ) ,,, odd value :'(
    #cv2.imshow("IMG",binarizedImage)
    #cv2.waitKey()
    #cv2.imwrite("images/skeletonizeThis.jpg",binarizedImage)
    #plt.imshow(binarizedImage,'gray')
    #plt.show()
    return binarizedImage








'''img = cv2.medianBlur(img, 5)
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
cv2.THRESH_BINARY, 11, 2)


th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
        cv2.THRESH_BINARY, 11, 2)
plt.title('Adaptive Gaussian Thresholding')
print(len(th3))
for i in th3
for i in range(len(th3)):
    for j in range(len(th3[0])):
        if(th3[i][j]==0):
            print(th3[i][j],end=" ")
plt.imshow(th3,'gray')
'''
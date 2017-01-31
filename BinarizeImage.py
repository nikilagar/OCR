import cv2

#from matplotlib import pyplot as plt


def getBinarizedImage(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    binarizedImage=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
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
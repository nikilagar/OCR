from BinarizeImage import *
import thinnigSkeletonization as tsk
import cv2
from matplotlib import pyplot as py
import componentGetter,extractingLines





image=getBinarizedImage("images/fuckingImage.jpg") #Getting Binarized image and Denoised image :)
image=tsk.getSkeletonizedImage(image)   #thinning image
cv2.imshow("SeeMe",image)   #showing image
cv2.waitKey()
print("hello")











'''extractingLines.doit(image)

components=componentGetter.getComponents(image)
print(len(components))
per=[]
pery=[0 for i in range(len(components))]
cenx=[];ceny=[]
for i in components:
    per.append(len(i))
    x=0.0;y=0.0
    for j in i:
        x=x+j[0]
        y=y+j[1]
    x/=len(i);y/len(i)
    cenx.append(x)
    ceny.append(y)
print(len(per),pery)
yper=[0 for i in range(len(per))]
#py.scatter(per,yper)
#print(components)



py.imshow(image,'gray')
py.show()
#print(image)
'''
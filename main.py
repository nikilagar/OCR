from BinarizeImage import *
import verticalProfile as vp
import horizontalProfile as hp
import Features
import pandas as pd
import numpy as np
import random
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier, VotingClassifier, GradientBoostingClassifier, ExtraTreesClassifier


image=cv2.imread("images/fIMage.jpg",0)
image=getBinarizedImage(image) #Getting Binarized image and Denoised image :)



#cv2.imshow("binarized",image)
#cv2.imshow("SeeMe",image)   #showing image
characters=vp.segment(image,hp.getPoints(image))


for i in characters:
    print(Features.getFeatures(image[i[0]:i[2]+1,i[1]:i[3]+1]))

#MACHINE
classification=[]
trainData=[]
for i in range(65,91):
    df = pd.read_csv('data/trdata'+chr(i)+'.csv')
    trainData += df.values.tolist()
    df = pd.DataFrame()
    df = pd.read_csv('data/clasArr'+chr(i)+'.csv')
    classification += df.values.tolist()[0]

X_trainData, X_test, y_trainData, y_test = train_test_split(trainData,classification, random_state=int(random.random()*1000))

alg = RandomForestClassifier(random_state=1, n_estimators=28, max_depth = 9, min_samples_split=10, min_samples_leaf=8)
alg.fit(X_trainData, y_trainData)
for i in characters:
    print(chr(alg.predict(Features.getFeatures(image[i[0]:i[2]+1,i[1]:i[3]+1]))[0]),end=" ")

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
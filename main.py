from sklearn.linear_model import LogisticRegression
import GUI
import normalizer
from matplotlib import pyplot as plt
from BinarizeImage import *
import verticalProfile as vp
import horizontalProfile as hp
import Features
import pandas as pd
import numpy as np
import random
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier, VotingClassifier, GradientBoostingClassifier, ExtraTreesClassifier
import sys

DataFolderPath="tmpdata1"

if(len(sys.argv)<2):
    image=cv2.imread("images/sampleInput.png",0)
else :
    image=cv2.imread(sys.argv[1],0)
image=getBinarizedImage(image) #Getting Binarized image and Denoised image :)



#cv2.imshow("binarized",image)
#cv2.imshow("SeeMe",image)   #showing image

charactersLineWise=[]
lines=hp.getPoints(image)
for i in lines:
    charactersLineWise.append(vp.segment(image,[i]))
'''
for characters in charactersLineWise:
    for i in characters:
        print(Features.getFeatures(image[i[0]:i[2]+1,i[1]:i[3]+1]))
'''

#MACHINE
classification=[]
trainData=[]
for i in range(65,91):
    df = pd.read_csv(DataFolderPath+ '/trdata'+chr(i)+'.csv')
    trainData += df.values.tolist()
    df = pd.DataFrame()
    df = pd.read_csv(DataFolderPath+'/clasArr'+chr(i)+'.csv')
    classification += df.values.tolist()[0]

DataFolderPath="tmpdata2small"
for i in range(97,123):
    df = pd.read_csv(DataFolderPath+ '/trdata'+chr(i)+'.csv')
    trainData += df.values.tolist()
    df = pd.DataFrame()
    df = pd.read_csv(DataFolderPath+'/clasArr'+chr(i)+'.csv')
    classification += df.values.tolist()[0]


X_trainData, X_test, y_trainData, y_test = train_test_split(trainData,classification, random_state=int(random.random()*1000))

#alg=LogisticRegression(C=.9, max_iter=80)
#alg = RandomForestClassifier(random_state=1, n_estimators=28, max_depth = 9, min_samples_split=10, min_samples_leaf=8)



alg = RandomForestClassifier(random_state=1, n_estimators=28, max_depth = 9, min_samples_split=10, min_samples_leaf=8)
alg1 = LogisticRegression(C=.9, max_iter=80)
alg2=ExtraTreesClassifier()

eclf1 = VotingClassifier(estimators=[('lr', alg1), ('etc', alg2), ('rfc', alg)], voting = 'soft')
eclf1 = eclf1.fit(trainData,classification)

for characters in charactersLineWise:
    for i in characters:
        croppedImage=image[i[0]:i[2]+1,i[1]:i[3]+1]
        probabMatrix=eclf1.predict_proba(Features.getFeatures(croppedImage))
        #print(probabMatrix)
        lis=[]
        for i in range(0,52):
            lis.append([probabMatrix[0][i],i])
        lis.sort(reverse=True)
        #print(lis)
        sortedLetters=[]
        for i in lis:
            if(i[0]>0):
                if(i[1]>=26):
                    sortedLetters.append([chr(71+i[1]),i[0]])
                else:
                    sortedLetters.append([chr(65+i[1]),i[0]])


        #GUI.buildGUI(alg.predict_proba(Features.getFeatures(croppedImage)),croppedImage)
        #cv2.imshow("After segmentation",croppedImage)
        #cv2.imshow("After normalization and thinning", croppedImage)

        print(chr(eclf1.predict(Features.getFeatures(croppedImage))[0]),end=" ")
        
        stri = "Candidates after classification, probability wise :::  \n"
        for i in range(0, min(5, len(sortedLetters))):
            stri += sortedLetters[i][0] + "(" + str(round(sortedLetters[i][1],2)) + ")" + " , "

        fig = plt.figure(figsize=(4.6, 4.6))
        ax = fig.add_subplot(1, 2, 1)
        ax.imshow(cv2.resize(croppedImage, (24, 24)), cmap='gray')
        ax.set_title("Segmented character")
        # plt.imshow(croppedImage,cmap='gray')
        ax = fig.add_subplot(122)
        ax.imshow(normalizer.getNormalizedImage(croppedImage), cmap='gray')
        ax.set_title("Thinned Image")
        plt.suptitle(stri)
        plt.show()
    print()



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
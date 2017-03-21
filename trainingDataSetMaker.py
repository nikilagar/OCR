import cv2
import horizontalProfile as hp
import verticalProfile as vp
import Features
import os
import pandas as pd

path="/home/nikhil/PycharmProjects/English/Fnt/Selected Fonts/Sample0"
currentChar=82
for smpl in range(28,37):
	trdata=[]
	clasArr=[]
	totalFiles=len(os.listdir(path+str(smpl)))
	for imno in range(min(200,totalFiles)):
		print(path+str(smpl)+"/"+str(imno)+".png")
		img=cv2.imread(path+str(smpl)+"/"+str(imno)+".png",0)

		i=vp.segment(img,hp.getPoints(img))
		zonFeatures=Features.getFeatures(img[i[0][0]:i[0][2] + 1, i[0][1]:i[0][3] + 1])
		trdata.append(zonFeatures)
		clasArr.append(currentChar)
		print(len(i))
	df=pd.DataFrame(trdata)
	df.to_csv("trdata"+chr(currentChar)+".csv",index=False)
	finClasArr=[clasArr]
	df=pd.DataFrame(finClasArr)
	df.to_csv("clasArr"+chr(currentChar)+".csv",index=False)
	currentChar+=1


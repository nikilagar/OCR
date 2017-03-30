import cv2
import horizontalProfile as hp
import verticalProfile as vp
import Features
import os
import pandas as pd

path="/home/nikhil/PycharmProjects/English/Fnt/Selected Fonts/Sample0"
DataFolderPath="tmpdata2small"
currentChar=97
for smpl in range(37,63):
	trdata=[]
	clasArr=[]
	totalFiles=len(os.listdir(path+str(smpl)))
	for imno in range(min(100,totalFiles)):
		print(path+str(smpl)+"/"+str(imno)+".png")
		img=cv2.imread(path+str(smpl)+"/"+str(imno)+".png",0)

		characters=vp.segment(img,hp.getPoints(img))
		x1,y1,x2,y2=len(img),len(img[0]),0,0
		print(characters)
		for i in characters:
			x1=min(x1,i[0])
			y1=min(y1,i[1])
			x2=max(x2,i[2])
			y2=max(y2,i[3])
		zonFeatures=Features.getFeatures(img[x1:x2 + 1, y1:y2 + 1])
		trdata.append(zonFeatures)
		clasArr.append(currentChar)
	df=pd.DataFrame(trdata)
	df.to_csv(DataFolderPath + "/trdata"+chr(currentChar)+".csv",index=False)
	finClasArr=[clasArr]
	df=pd.DataFrame(finClasArr)
	df.to_csv(DataFolderPath + "/clasArr"+chr(currentChar)+".csv",index=False)
	currentChar+=1


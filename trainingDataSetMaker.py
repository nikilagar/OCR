import cv2
import horizontalProfile as hp
import verticalProfile as vp
import Features
import os

for smple in range(65,91):
    path="../English/Chosen/Sample0"+str(smple)
    totalFiles=len(os.listdir(path))
    for imno in range(totalFiles):
        img=cv2.imread(path+"/"+str(imno)+".png",0)
        characters=vp.segment(img,hp.getPoints(img))
        print(len(characters))
        for i in characters:
            print(Features.getFeatures(img[i[0]:i[2] + 1, i[1]:i[3] + 1]))

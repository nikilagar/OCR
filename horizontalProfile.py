def getPoints(img):
    imgx,imgy=len(img),len(img[0])
    x=[];y=[];finalPts=[]
    for i in range (imgx):
        bpixcnt=0
        for j in range (imgy):
            if img[i][j]==0:
                bpixcnt+=1
        x.append(i);y.append(bpixcnt)
    i=0;
    while i<imgx:
        f=False
        if(y[i]>0):
            f=True
            pr=i
        while i<imgx and y[i]>0:
            i+=1
        if(f==True):
            finalPts.append([pr,i-1])
            i-=1
        i+=1
    #plt.show()
    return finalPts

from matplotlib import pyplot as py
def doit(image):
    perx=[]
    pery=[]
    global perx,pery
    for i in range(len(image)):
        cn=0
        for j in range(len(image[0])):
            if(image[i][j]==0):
                cn+=1
        perx.append(i)
        pery.append(cn)
    print(perx)
    print(pery)
    py.scatter(perx,pery)
    py.show()
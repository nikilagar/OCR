dir=[[1, 1, 1, 0, 0, -1, -1, -1], [-1, 0, 1, -1, 1, 1, 0, -1]]
imageWidth=int()
imageHeight=int()
imgMatrix=[[]]
comp=[]
lis=[[]]
vis=[[0 for j in range(800)] for i in range(1400)]

def validate(x, y):
    if(x<0 or y<0 or y>=imageWidth or x>=imageHeight ):
        return False
    return True

def dfs(i,j):
    global dir,imgMatrix,vis,lis
    vis[i][j]=1
    if(imgMatrix[i][j]!=0):
        return
    for k in range(0,8):
        x=i+dir[0][k]
        y=j+dir[1][k]
        if(validate(x, y)==True and imgMatrix[x][y]==0 and vis[x][y]==0):
            lis.append([x,y]);dfs(x,y)
def getComponents(imgMatri):
    global imageWidth,imageHeight,imgMatrix,comp,lis,vis
    imageWidth=len(imgMatri[0])
    imageHeight=len(imgMatri)
    imgMatrix=imgMatri
    for i in range(imageHeight):
        for j in range(imageWidth):
            lis=[]
            fl=0
            if(imgMatrix[i][j]==0 and vis[i][j]==0):
                fl=1;lis.append([i,j]);dfs(i,j)
            if fl==1 :
                comp.append(lis)
    return comp

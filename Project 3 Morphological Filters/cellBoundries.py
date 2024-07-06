# Michael Rizig
# Project 3: Morphological Filers
# 001008703
# File 2: Morph1
# 7/6/2024

#Import nessessary tools
import matplotlib.pyplot as plottool
import cv2
from skimage import io
import numpy as np

def erosion(i,j):
    s=0
    s= padded[i-1][j-1][0]*struct[0][0]+padded[i-1][j][0]*struct[0][1]+padded[i-1][j + 1][0]*struct[0][2]+padded[i][j-1][0]*struct[1][0]+ padded[i][j][0]*struct[1][1]+padded[i][j + 1][0]*struct[1][2]+padded[i + 1][j-1][0]*struct[2][0]+padded[i + 1][j][0]*struct[2][1]+padded[i + 1][j + 1][0]*struct[2][2]     
    if s>1024: # value chosed bc 256 * 4 = 1024, if the value is greater than 1024, than 5 pixels must have been hit
        return [255,255,255]
    return [0,0,0]
def connectedComponentAnalysis():
  
   
    #create static identifier for unique values
    id = 1  
    #loop through image
    for i in range(1,cellsImage.shape[0]):
        for j in range(1,cellsImage.shape[1]):
            if padded[i][j][0] >0 and componentsArray[i][j]==0:
                dfs(padded,i,j,id)
                id+=1
    print(id)
    ccomponentsArray = componentsArray[0:componentsArray.shape[0]-20,0:componentsArray.shape[1]]
    for i in range(1,ccomponentsArray.shape[0]-1):    
        for j in range(1,ccomponentsArray.shape[1]-1):
            if ccomponentsArray[i+1][j] < ccomponentsArray[i][j] and ccomponentsArray[i+1][j]!=0:
                ccomponentsArray[i][j] = ccomponentsArray[i+1][j]
            if ccomponentsArray[i+1][j+1] < ccomponentsArray[i][j] and ccomponentsArray[i+1][j+1]!=0:
                ccomponentsArray[i][j] = ccomponentsArray[i+1][j+1]
            if ccomponentsArray[i][j+1] < ccomponentsArray[i][j] and ccomponentsArray[i][j+1]!=0:
                ccomponentsArray[i][j] = ccomponentsArray[i][j+1]
            if ccomponentsArray[i-1][j+1] < ccomponentsArray[i][j] and ccomponentsArray[i-1][j+1]!=0:
                ccomponentsArray[i][j] = ccomponentsArray[i-1][j+1]
            if ccomponentsArray[i-1][j] < ccomponentsArray[i][j] and ccomponentsArray[i-1][j]!=0:
                ccomponentsArray[i][j] = ccomponentsArray[i-1][j]
            if ccomponentsArray[i-1][j-1] < ccomponentsArray[i][j] and ccomponentsArray[i-1][j-1]!=0:
                ccomponentsArray[i][j] = ccomponentsArray[i-1][j-1]
            if ccomponentsArray[i][j-1] < ccomponentsArray[i][j] and ccomponentsArray[i][j-1]!=0:
                ccomponentsArray[i][j] = ccomponentsArray[i][j-1]
            if ccomponentsArray[i+1][j-1] < ccomponentsArray[i][j] and ccomponentsArray[i+1][j-1]!=0:
                ccomponentsArray[i][j] = ccomponentsArray[i+1][j-1]
    
    count=0
    last=[]
    for i in range(ccomponentsArray.shape[0]):
        for j in range(ccomponentsArray.shape[1]):
            if ccomponentsArray[i][j]!=0 and last.count(ccomponentsArray[i][j])==0 :
                count+=1
                last.append(ccomponentsArray[i][j])
    print("Number of unique cells: ", count)
    print(last)

def dfs(image, i, j , id):
    
    #create stack for depth first search
    stack = []
    componentsArray[i][j] = id
    while True:
        for p in range(-1,2):
            for q in range(-1,2):
                if image[(i+p)%image.shape[0]-1][j+q][0]!=0 and componentsArray[(i+p)%image.shape[0]-2][j+q]==0:
                    stack.append((i+p,j+q))
                    componentsArray[(i+p)%image.shape[0]-2][j+q]=id
        if len(stack)==0:
            break

        val = stack.pop()
        componentsArray[val[0]%image.shape[0]-2,val[1]] = id
        i,j = val

struct = [[0,1,0],[1,1,1],[0,1,0]]

#define image path for cell image
cellsPath = 'input/cell.jpg'

#load image
cellsImage = io.imread(cellsPath)

#color correction
cellsImage = cv2.cvtColor(cellsImage, cv2.COLOR_BGR2RGB)

output = cellsImage.copy()
#threshold the image

for i in range (cellsImage.shape[0]):
    for j in range(cellsImage.shape[1]):
        if cellsImage[i][j][0] > 10:
            cellsImage[i][j]=[255,255,255]
        else:
            cellsImage[i][j] = [0,0,0]


#pad image 
padded = cv2.copyMakeBorder(cellsImage,1,1,1,1,cv2.BORDER_CONSTANT,value=[0,0,0])
#plottool.imshow(cellsImage)
#plottool.show()
#create an array of integers to store where each connected component is
componentsArray = np.full((cellsImage.shape[0],cellsImage.shape[1],1),0,dtype=int)
for i in range (cellsImage.shape[0]):
    for j in range(cellsImage.shape[1]):
        output[i][j] = erosion(i,j)
cellsImage = output

#display original image
#plottool.imshow(cellsImage)
#plottool.show()

connectedComponentAnalysis()

plottool.imshow(componentsArray)
plottool.savefig('output/morph/cells/CCA.png')
plottool.show()


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
import sys

def connectedComponentAnalysis():
  
   
    #create static identifier for unique values
    id = 1  
    #loop through image
    for i in range(1,cellsImage.shape[0]):
        for j in range(1,cellsImage.shape[1]):
            if padded[i][j][0] >10 and componentsArray[i][j]==0:
                dfs(padded,i,j,id)
                id+=1
    print(id)
    for i in range(1,cellsImage.shape[0]-1):    
        for j in range(1,cellsImage.shape[1]-1):
            if componentsArray[i+1][j] < componentsArray[i][j] and componentsArray[i+1][j]!=0:
                componentsArray[i][j] = componentsArray[i+1][j]
            if componentsArray[i+1][j+1] < componentsArray[i][j] and componentsArray[i+1][j+1]!=0:
                componentsArray[i][j] = componentsArray[i+1][j+1]
            if componentsArray[i][j+1] < componentsArray[i][j] and componentsArray[i+1][j+1]!=0:
                componentsArray[i][j] = componentsArray[i][j+1]
            if componentsArray[i-1][j+1] < componentsArray[i][j] and componentsArray[i-1][j+1]!=0:
                componentsArray[i][j] = componentsArray[i-1][j+1]
            if componentsArray[i-1][j] < componentsArray[i][j] and componentsArray[i-1][j]!=0:
                componentsArray[i][j] = componentsArray[i-1][j]
            if componentsArray[i-1][j-1] < componentsArray[i][j] and componentsArray[i-1][j-1]!=0:
                componentsArray[i][j] = componentsArray[i-1][j-1]
            if componentsArray[i][j-1] < componentsArray[i][j] and componentsArray[i][j-1]!=0:
                componentsArray[i][j] = componentsArray[i][j-1]
            if componentsArray[i+1][j-1] < componentsArray[i][j] and componentsArray[i+1][j-1]!=0:
                componentsArray[i][j] = componentsArray[i+1][j-1]
    
    count=0
    last=[]
    for i in range(componentsArray.shape[0]):
        for j in range(componentsArray.shape[1]):
            if componentsArray[i][j]!=0 and last.count(componentsArray[i][j])==0 :
                count+=1
                last.append(componentsArray[i][j])
    print("Number of unique cells: ", count)

def dfs(image, i, j , id):
    
    #create stack for depth first search
    stack = []
    componentsArray[i][j] = id
    """if(image[i+1][j+1][0]!=0 and componentsArray[i+1][j+1]==0):
            stack.append((i+1,j+1))
            componentsArray[i+1][j+1] = id
        if(image[i+1][j][0]!=0 and componentsArray[i+1][j]==0):
            stack.append((i+1,j))
            componentsArray[i+1][j] = id
        if(image[i+1][j-1][0]!=0 and componentsArray[i+1][j-1]==0):
            stack.append((i+1,j+1))
            componentsArray[i+1][j-1] = id
        if(image[i][j+1][0]!=0 and componentsArray[i][j+1]==0):
            stack.append((i,j+1))
            componentsArray[i][j+1] = id
        if(image[i][j-1][0]!=0 and componentsArray[i][j-1]==0):
            stack.append((i,j-1))
            componentsArray[i][j-1] = id
        if(image[i-1][j-1][0]!=0 and componentsArray[i-1][j-1]==0):
            stack.append((i-1,j-1))
            componentsArray[i-1][j-1] = id
        if(image[i-1][j+1][0]!=0 and componentsArray[i-1][j+1]==0):
            stack.append((i-1,j+1))
            componentsArray[i-1][j+1] = id
        if(image[i-1][j][0]!=0 and componentsArray[i-1][j]==0):
            stack.append((i-1,j))
            componentsArray[i-1][j] = id"""

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



#define image path for cell image
cellsPath = 'input/cell.jpg'

#load image
cellsImage = io.imread(cellsPath)

#color correction
cellsImage = cv2.cvtColor(cellsImage, cv2.COLOR_BGR2RGB)

#threshold the image

for i in range (cellsImage.shape[0]):
    for j in range(cellsImage.shape[1]):
        if cellsImage[i][j][0] > 10:
            cellsImage[i][j]=[255,255,255]
        else:
            cellsImage[i][j] = [0,0,0]



#pad image 
padded = cv2.copyMakeBorder(cellsImage,1,1,1,1,cv2.BORDER_CONSTANT,value=[0,0,0])

#create an array of integers to store where each connected component is
componentsArray = np.full((cellsImage.shape[0],cellsImage.shape[1],1),0,dtype=int)

#display original image
plottool.imshow(cellsImage)
plottool.show()

connectedComponentAnalysis()

plottool.imshow(componentsArray)
plottool.savefig('output/morph/cells/CCA.png')
plottool.show()


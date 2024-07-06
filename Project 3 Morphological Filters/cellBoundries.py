# Michael Rizig
# Project 3: Morphological Filers
# 001008703
# File 3: Cell Boundries
# 7/6/2024

#Import nessessary tools
import matplotlib.pyplot as plottool
import cv2
from skimage import io
import numpy as np
import random

#same erosion function found in previous file (morphologicalprocessing.py)
def erosion(i,j):
    s=0
    s= padded[i-1][j-1][0]*struct[0][0]+padded[i-1][j][0]*struct[0][1]+padded[i-1][j + 1][0]*struct[0][2]+padded[i][j-1][0]*struct[1][0]+ padded[i][j][0]*struct[1][1]+padded[i][j + 1][0]*struct[1][2]+padded[i + 1][j-1][0]*struct[2][0]+padded[i + 1][j][0]*struct[2][1]+padded[i + 1][j + 1][0]*struct[2][2]     
    if s>1024: # value chosed bc 256 * 4 = 1024, if the value is greater than 1024, than 5 pixels must have been hit
        return [255,255,255]
    return [0,0,0]

#this function is to determine which components are conneceted
def connectedComponentAnalysis():
    #create static identifier for unique values
    id = 100 

    #step 1: first pass to give temperary id to elements
    #loop through image
    for i in range(1,cellsImage.shape[0]):
        for j in range(1,cellsImage.shape[1]):
            #if a value is not 0 and has not been id'd yet
            if padded[i][j][0] >0 and componentsArray[i][j]==0:
                # call depth first seatch on this pixel
                dfs(padded,i,j,id)
                #update id
                id+=50
    # correct for previous padding            
    ccomponentsArray = componentsArray[0:componentsArray.shape[0]-20,0:componentsArray.shape[1]]
    
    #step 2: combine connected id's to find final number
    # this nested loop below compares each pixel to its 8-nieghbors and choses the smallest value of the bunch
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

    #finally we count how many values are total after combining
    count=0
    last=[]
    for i in range(ccomponentsArray.shape[0]):
        for j in range(ccomponentsArray.shape[1]):
            if ccomponentsArray[i][j]!=0 and last.count(ccomponentsArray[i][j])==0 :
                count+=1
                last.append(ccomponentsArray[i][j])
    
    #how many unique numbers = unique cells 
    print("Number of unique cells: ", count)
    
    #change label values for colors to look more unique in image
    for i in range(ccomponentsArray.shape[0]):
        for j in range(ccomponentsArray.shape[1]):
            ccomponentsArray[i][j] = ccomponentsArray[i][j]
    
    #return our components array
    return ccomponentsArray, count        

#simple depth first search to find each connected component
def dfs(image, i, j , id):
    
    #create stack for depth first search
    stack = []

    #id current pixel
    componentsArray[i][j] = id

    #dfs, adding each un-id'd to the stack an id'ing it, then popping next element off stack 
    while True:
        for p in range(-1,2):
            for q in range(-1,2):
                if image[(i+p)%image.shape[0]-1][j+q][0]!=0 and componentsArray[(i+p)%image.shape[0]-2][j+q]==0:
                    stack.append((i+p,j+q))
                    componentsArray[(i+p)%image.shape[0]-2][j+q]=id
        
        #base case (to break out of loop eventually)
        if len(stack)==0:
            break
        
        #move on to next stack value
        val = stack.pop()
        #id next stack value
        componentsArray[val[0]%image.shape[0]-2,val[1]] = id
        #update i,j so we continue to move around image
        i,j = val


#define image path for cell image
cellsPath = 'input/cell.jpg'

#load image
cellsImage = io.imread(cellsPath)

#color correction
cellsImage = cv2.cvtColor(cellsImage, cv2.COLOR_BGR2RGB)

#display original imge
plottool.imshow(cellsImage)
plottool.show()

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

#define structure for erosion
struct = [[0,1,0],[1,1,1],[0,1,0]]

#define output for erosion
output = cellsImage.copy()

#erode image to remove any extruding inperfections that may interfere with our algoritm
for i in range (cellsImage.shape[0]):
    for j in range(cellsImage.shape[1]):
        output[i][j] = erosion(i,j)

#update image to our eroded image
cellsImage = output

#display image after threshold and erosion
plottool.imshow(cellsImage)
plottool.savefig('output/morph/cells/thresholded&Eroded.png')
plottool.show()

#apply connected component analysis to determine how many cells are in the image
out, count = connectedComponentAnalysis()

#display output of connected component function
plottool.imshow(out)
#plottool.savefig('output/morph/cells/CCA.png')
plottool.show()

#create array to hold count values
cellSizes = [0 for i in range(count)]
values = []

# find all unique values from image
for i in range (out.shape[0]):
    for j in range(out.shape[1]):
        if out[i][j]!=0 and values.count(out[i][j])==0:
            values.append(out[i][j])

#count each unique value and store it in cellSizes array
for i in range (out.shape[0]):
    for j in range(out.shape[1]):
        if out[i][j]!=0:
            cellSizes[values.index(out[i][j])]+=1
#display sizes of cells
print(values)
print(cellSizes)

#find label for largest cell
largestCell = values[cellSizes.index(max(cellSizes))]

#create an image to store original bounds of largest cell
largestOriginalBound = out.copy()

#find largest bounds
for i in range(largestOriginalBound.shape[0]):
    for j in range(largestOriginalBound.shape[1]):
        largestOriginalBound[i][j]=0
        if out[i][j] == largestCell:
            largestOriginalBound[i][j] = largestCell

#show largst cell 
plottool.imshow(largestOriginalBound)
plottool.title("Largest Cell")
plottool.savefig('output/morph/cells/largestCell.png')
plottool.show()

#now we erode the image using the same struct as before but now with respect to only the largst cell
#output for erosion
boundryOut = out.copy()

#erosion process
for i in range (out.shape[0]-1):
    for j in range(out.shape[1]-1):
        #same as erosion function from previous file(morphologicalProcessing.py)
        s= out[i-1][j-1][0]*struct[0][0]+out[i-1][j][0]*struct[0][1]+out[i-1][j + 1][0]*struct[0][2]+out[i][j-1][0]*struct[1][0]+ out[i][j][0]*struct[1][1]+out[i][j + 1][0]*struct[1][2]+out[i + 1][j-1][0]*struct[2][0]+out[i + 1][j][0]*struct[2][1]+out[i + 1][j + 1][0]*struct[2][2]     
        # if s = largestcell*5, then all 5 pixels in filter hit a largest cell value, so make target pixel largest cell value
        if s==largestCell*5:
            boundryOut[i][j]=largestCell
        else:
            #else set to 0
            boundryOut[i][j]=0

#display eroded largest cell
plottool.imshow(boundryOut)
plottool.title("erosion with respect to largest only")
plottool.savefig('output/morph/cells/erodedlargest.png')
plottool.show()

#subtract eroded cell from original to get boundry
largestOriginalBound-=boundryOut

#finally, display boundry.
plottool.imshow(largestOriginalBound)
plottool.title("Largest minus eroded largest")
plottool.savefig('output/morph/cells/LargestMinusErodedLargest.png')
plottool.show()
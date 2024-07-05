# Michael Rizig
# Project 3: Morphological Filers
# 001008703
# File 1: Sharpening
# 7/5/2024

#Import nessessary tools
import matplotlib.pyplot as plottool
import cv2
from skimage import io
import numpy as np
# below function defines the which is the sharpening filter used 

def laplacian(i,j):
    s= padded[i-1, j-1]*lapFilter[0][0]+padded[i-1, j]*lapFilter[0][1]+padded[i-1, j + 1]*lapFilter[0][2]+padded[i, j-1]*lapFilter[1][0]+ padded[i][j]*lapFilter[1][1]+padded[i, j + 1]*lapFilter[1][2]+padded[i + 1, j-1]*lapFilter[2][0]+padded[i + 1, j]*lapFilter[2][1]+padded[i + 1, j + 1]*lapFilter[2][2]     
    if(s[1]<0):
        return 256- s
    return s
def sobel(i,j):
    s=0
    #take the defined sobel mask/filter and apply it to each pixel in the range x-1,y-1 to x+1,y+1
    #this time, since the values differ in each step, instead of a loop i decide to one line it
    s= padded[i-1, j-1]*sobelV[0][0]+padded[i-1, j]*sobelV[0][1]+padded[i-1, j + 1]*sobelV[0][2]+padded[i, j-1]*sobelV[1][0]+ padded[i][j]*sobelV[1][1]+padded[i, j + 1]*sobelV[1][2]+padded[i + 1, j-1]*sobelV[2][0]+padded[i + 1, j]*sobelV[2][1]+padded[i + 1, j + 1]*sobelV[2][2]     
    s+= padded[i-1, j-1]*sobelH[0][0]+padded[i-1, j]*sobelH[0][1]+padded[i-1, j + 1]*sobelH[0][2]+padded[i, j-1]*sobelH[1][0]+ padded[i][j]*sobelH[1][1]+padded[i, j + 1]*sobelH[1][2]+padded[i + 1, j-1]*sobelH[2][0]+padded[i + 1, j]*sobelH[2][1]+padded[i + 1, j + 1]*sobelH[2][2]     

    if(s[1]<0):
        return 256- s
    return s 

lapFilter = [[1,1,1],[1,-8,1],[1,1,1]]
#sobel filters vertical and horizontal from slides:
sobelV = [[-1,-2,-1],[0,0,0],[1,2,1]]
sobelH = [[-1,0,1],[-2,0,2],[-1,0,1]]

path = 'input/moon.jpg'
moonimage = io.imread(path)
moonimage = cv2.cvtColor(moonimage,cv2.COLOR_BGR2RGB)
padded = cv2.copyMakeBorder(moonimage,1,1,1,1,cv2.BORDER_CONSTANT,value=[0,0,0])

output = moonimage.copy()
lapic = np.zeros([moonimage.shape[0], moonimage.shape[1], 3], dtype=np.uint8)

sob = np.zeros([moonimage.shape[0], moonimage.shape[1], 3], dtype=np.uint8)
plottool.imshow(padded)
plottool.show()

for i in range(moonimage.shape[0]):
   for j in range(moonimage.shape[1]):
        lapic[i][j] = laplacian(i,j) 
        output[i][j] = output[i][j]+lapic[i][j]

plottool.imshow(lapic)
plottool.show()
#cv2.imwrite('output/sharpen/laplacian/laplacianFilter1.jpg',lapic)
plottool.imshow(output)
plottool.show()
#cv2.imwrite('output/sharpen/laplacian/outLaplace.jpg',output)

output = moonimage.copy()
for i in range(moonimage.shape[0]):
   for j in range(moonimage.shape[1]):
        sob[i][j] = sobel(i,j) 

output=output + sob
plottool.imshow(sob)
plottool.show()
cv2.imwrite('output/sharpen/sobel/sobelFilter.jpg',sob)
plottool.imshow(output)
plottool.show()
cv2.imwrite('output/sharpen/sobel/outSobel.jpg',output)

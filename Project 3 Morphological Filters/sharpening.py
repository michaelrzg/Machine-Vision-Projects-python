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
    #instead of using loops, im utilizing linear alg to turn the filter into a linar combinaiton of the two maticies. (c1v1 + c2v2 .. cmvm)
    s= padded[i-1, j-1]*lapFilter[0][0]+padded[i-1, j]*lapFilter[0][1]+padded[i-1, j + 1]*lapFilter[0][2]+padded[i, j-1]*lapFilter[1][0]+ padded[i][j]*lapFilter[1][1]+padded[i, j + 1]*lapFilter[1][2]+padded[i + 1, j-1]*lapFilter[2][0]+padded[i + 1, j]*lapFilter[2][1]+padded[i + 1, j + 1]*lapFilter[2][2]     
    #correcting for negative values by taking absolute value
    if(s[1]<0):
        return 256- s
    return s
def sobel(i,j):
    s=0
    #take the defined sobel mask/filter and apply it to each pixel in the range x-1,y-1 to x+1,y+1
    #as before, we are utilizing linar combinations.
    #one pass for vertical
    s= padded[i-1, j-1]*sobelV[0][0]+padded[i-1, j]*sobelV[0][1]+padded[i-1, j + 1]*sobelV[0][2]+padded[i, j-1]*sobelV[1][0]+ padded[i][j]*sobelV[1][1]+padded[i, j + 1]*sobelV[1][2]+padded[i + 1, j-1]*sobelV[2][0]+padded[i + 1, j]*sobelV[2][1]+padded[i + 1, j + 1]*sobelV[2][2]     
    #one pass for horizontal 
    s+= padded[i-1, j-1]*sobelH[0][0]+padded[i-1, j]*sobelH[0][1]+padded[i-1, j + 1]*sobelH[0][2]+padded[i, j-1]*sobelH[1][0]+ padded[i][j]*sobelH[1][1]+padded[i, j + 1]*sobelH[1][2]+padded[i + 1, j-1]*sobelH[2][0]+padded[i + 1, j]*sobelH[2][1]+padded[i + 1, j + 1]*sobelH[2][2]     
    
    #correcting for negative values by taking absolute value
    if(s[1]<0):
        return 256- s
    return s 

#define lapical filter we are using (from slides):
lapFilter = [[1,1,1],[1,-8,1],[1,1,1]]

#sobel filters vertical and horizontal (from slides):
sobelV = [[-1,-2,-1],[0,0,0],[1,2,1]]
sobelH = [[-1,0,1],[-2,0,2],[-1,0,1]]

#define path
path = 'input/moon.jpg'

#read image
moonimage = io.imread(path)
#cvt color
moonimage = cv2.cvtColor(moonimage,cv2.COLOR_BGR2RGB)
#created padded version (for edges of image)
padded = cv2.copyMakeBorder(moonimage,1,1,1,1,cv2.BORDER_CONSTANT,value=[0,0,0])

#define an output image to be same dimentions etc as input
output = moonimage.copy()
#create a blank image for lapician filter results
lapic = np.zeros([moonimage.shape[0], moonimage.shape[1], 3], dtype=np.uint8)

#create a blank image for sobel filter results
sob = np.zeros([moonimage.shape[0], moonimage.shape[1], 3], dtype=np.uint8)

#display initial image
plottool.imshow(padded)
plottool.show()

#apply lapician image enhancement
for i in range(moonimage.shape[0]):
   for j in range(moonimage.shape[1]):
        lapic[i][j] = laplacian(i,j) 
        output[i][j] = output[i][j]+lapic[i][j]

#display the lapician filter generated
plottool.imshow(lapic)
plottool.show()

#save filter
#cv2.imwrite('output/sharpen/laplacian/laplacianFilter1.jpg',lapic)

#display output image (output - lapican filter generated)
plottool.imshow(output)
plottool.show()

#save output
#cv2.imwrite('output/sharpen/laplacian/outLaplace.jpg',output)

#reset output for sobel 
output = moonimage.copy()

#apply sobel
for i in range(moonimage.shape[0]):
   for j in range(moonimage.shape[1]):
        sob[i][j] = sobel(i,j) 

#combine sobel 
output=output + sob

#display the sobel filter generated
plottool.imshow(sob)
plottool.show()
#save filter
cv2.imwrite('output/sharpen/sobel/sobelFilter.jpg',sob)

#display output image (output - sobel filter generated)
plottool.imshow(output)
plottool.show()

#save output
cv2.imwrite('output/sharpen/sobel/outSobel.jpg',output)

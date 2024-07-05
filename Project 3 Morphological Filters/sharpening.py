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
def lapician(x,y,size=3):
    #init a sum varible to 0
    s =0 
    #loop through the filter size. (same as project 2 noise reduction average filtering)
    # by dividing the filter size by 2, then going to the left and right by the quotent, we are essentially centering the filter
    # ive done this by setting the range from -(size of filter)/2 to (size of filter)/2 +1, then taking floor of these values
    # for example , with filter size 3, we get range -1,2, meaning our filter will span:
    # [i-1,j-1] [i-1,j] [i-1,j+1]
    # [i,  j-1] [i,  j] [i,  j+1]
    # [i+1,j-1] [i+1,j] [i+1,j+1]
    for i in range(-int(size/2),int(size/2)+1):
       for j in range(-int(size/2),int(size/2)+1):
        #for each value we determine its position in the filter, and multiply its coeffient to it and add it to sum
        #if it is the center pixel, multiply by 8 add add:
            s+= -1* padded[x+i][y+j] 
    s+= 9 * padded[x][y]
    #finally return the sum
    if s[0]<0:
        s*= -1
    return s 

def sobel(i,j):
    s=0
    #take the defined sobel mask/filter and apply it to each pixel in the range x-1,y-1 to x+1,y+1
    #this time, since the values differ in each step, instead of a loop i decide to one line it
    
    s= padded[i-1, j-1]*sobelV[0][0]+padded[i-1, j]*sobelV[0][1]+padded[i-1, j + 1]*sobelV[0][2]+padded[i, j-1]*sobelV[1][0]+ padded[i][j]*sobelV[1][1]+padded[i, j + 1]*sobelV[1][2]+padded[i + 1, j-1]*sobelV[2][0]+padded[i + 1, j]*sobelV[2][1]+padded[i + 1, j + 1]*sobelV[2][2]     
    return s 

#sobel filters vertical and horizontal from slides:
sobelV = [[-1,-2,-1],[0,0,0],[1,2,1]]
sobelH = [[-1,0,1],[-2,0,2],[-1,0,1]]

path = 'input/moon.jpg'
moonimage = io.imread(path)
moonimage = cv2.cvtColor(moonimage,cv2.COLOR_BGR2RGB)
padded = cv2.copyMakeBorder(moonimage,1,1,1,1,cv2.BORDER_CONSTANT,value=[0,0,0])

output = moonimage.copy()
lapic = moonimage.copy()
sob = moonimage.copy()
plottool.imshow(padded)
plottool.show()

for i in range(moonimage.shape[0]):
   for j in range(moonimage.shape[1]):
        lapic[i][j] = lapician(i,j) 
       
output = output + lapic
plottool.imshow(lapic)
plottool.show()
#cv2.imwrite('output/sharpen/laplacian/laplacianFilter.jpg',lapic)
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

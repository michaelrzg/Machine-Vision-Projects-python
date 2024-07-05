# Michael Rizig
# Project 3: Morphological Filers
# 001008703
# File 2: Morph1
# 7/5/2024

#Import nessessary tools
import matplotlib.pyplot as plottool
import cv2
from skimage import io
import numpy as np

def tresh(x):
    if x>150:
        return [0,0,0]
    return [255,255,255]

def dialation(i,j):
    s=0
    s= padded[i-1, j-1]*struct[0][0]+padded[i-1, j]*struct[0][1]+padded[i-1, j + 1]*struct[0][2]+padded[i, j-1]*struct[1][0]+ padded[i][j]*struct[1][1]+padded[i, j + 1]*struct[1][2]+padded[i + 1, j-1]*struct[2][0]+padded[i + 1, j]*struct[2][1]+padded[i + 1, j + 1]*struct[2][2]     
    if s[0]>0:
        return [255,255,255]
    return [0,0,0]

def erosion(i,j):
    s=0
    s= padded[i-1][j-1][0]*struct[0][0]+padded[i-1][j][0]*struct[0][1]+padded[i-1][j + 1][0]*struct[0][2]+padded[i][j-1][0]*struct[1][0]+ padded[i][j][0]*struct[1][1]+padded[i][j + 1][0]*struct[1][2]+padded[i + 1][j-1][0]*struct[2][0]+padded[i + 1][j][0]*struct[2][1]+padded[i + 1][j + 1][0]*struct[2][2]     
    if s>1024: # value chosed bc 256 * 4 = 1024, if the value is greater than 1024, than 5 pixels must have been hit
        return [255,255,255]
    return [0,0,0]
#image path
impath = 'input/fingerprint.jpg'

#import image
fingerprint = io.imread(impath)

#fix colors
fingerprint = cv2.cvtColor(fingerprint,cv2.COLOR_BGR2RGB)



#create ouput image:
output = fingerprint.copy()
#display image
plottool.imshow(fingerprint)
plottool.show()

#calculate histogram for image using cv2
hist = cv2.calcHist([fingerprint], [0], None, [256], [0,256])

#display original image's histogram distribution
plottool.plot(hist)
plottool.title("Fingerprint image Histogram Dist:")
plottool.savefig('output/morph/finger/hist.png')
plottool.show()

#define output for thresholding
thresholdImage = fingerprint.copy()

#apply threshold function
for i in range(fingerprint.shape[0]):
    for j in range(fingerprint.shape[1]):
        thresholdImage[i][j] = tresh(fingerprint[i][j][0])

#display results of threshold
plottool.imshow(thresholdImage)
plottool.show()

#created padded verion for filtering:
padded = cv2.copyMakeBorder(thresholdImage,1,1,1,1,cv2.BORDER_CONSTANT,value=[0,0,0])

#save threshold image
cv2.imwrite('output/morph/finger/thresh.jpg',thresholdImage)

#define structuring element:
struct = [[0,1,0],[1,1,1],[0,1,0]]

#dialate image:
for i in range(fingerprint.shape[0]):
    for j in range(fingerprint.shape[1]):
        output[i][j] = dialation(i,j)

#display results of dialation
plottool.imshow(output)
plottool.show()

#save results for dialation 
cv2.imwrite('output/morph/finger/dialated.jpg',output)

#updated padded
padded =  cv2.copyMakeBorder(output,1,1,1,1,cv2.BORDER_CONSTANT,value=[0,0,0])

#erode image:
for i in range(fingerprint.shape[0]):
    for j in range(fingerprint.shape[1]):
        output[i][j] = erosion(i,j)
  
#display results of erosion
plottool.imshow(output)
plottool.show()

#save results for erosion 
cv2.imwrite('output/morph/finger/eroded.jpg',output)
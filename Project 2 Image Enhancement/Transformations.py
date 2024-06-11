# Michael Rizig
# Project 2: Image Enhancement
# 001008703
# File 1: Transformation
# 6/11/2024

from skimage import io
import matplotlib.pyplot as plottool
import cv2
import math
uniPath = 'input/university.png'
image = io.imread(uniPath)
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
out = image.copy()

plottool.imshow(image)
plottool.show()
# log transformation with varying gamma:
gamma = [30,50,70,90,120,150]
for k in range(6):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            f = math.log10(1+ image[i][j][1]) *gamma[k]
            out[i][j] = [f,f,f]
    plottool.imshow(out)
    plottool.show()
    out=image.copy()
    
# power law transformation with varying gamma:
yValue = [.6,.9,1,1.2,1.3,1.4,1.5]
for k in range(6):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            f = math.pow(image[i][j][1],yValue[k]) 
            out[i][j] = [f,f,f]
    plottool.imshow(out)
    plottool.show()
    out=image.copy()
plottool.imshow(out)

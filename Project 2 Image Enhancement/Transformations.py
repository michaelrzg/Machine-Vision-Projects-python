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
# log transformation with varying constant factors:
constant = [30,50,70,90,120,150]
for k in range(6):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            f = math.log10(1+ image[i][j][1]) *constant[k]
            out[i][j] = [f,f,f]
    plottool.imshow(out)
    plottool.title(f'y = log(1+ x) * {constant[k]}')
    plottool.show()
    cv2.imwrite(f'output/log/logConstant-{constant[k]}.png',out)
    out=image.copy()
    
# power law transformation with varying gamma:
yValue = [.9,.8,.7,.6,.5,.4]
gamma = [1,1.5,2.2]
for l in range(3):
    for k in range(6):
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                f = math.pow(image[i][j][1]/255,(yValue[k]/gamma[l]))*255
                out[i][j] = [f,f,f]
        plottool.imshow(out)
        plottool.title( f'y={yValue[k]}, gamma={gamma[l]}') 
        plottool.show()
        cv2.imwrite(f'output/power/gamma-{gamma[l]}/yValue-{yValue[k]}.png',out)
        out=image.copy()
plottool.imshow(out)


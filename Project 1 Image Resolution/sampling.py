# Michael Rizig
# Project 1: Digital Image Processing
# File 1: Sampling
# 6/4/2024

#nessessary imports:
from skimage import io
import matplotlib.pyplot as plottool
import numpy as np
import cv2

#read in image:
imagePath = 'input/cat.jpg'
alqita = io.imread(imagePath)

image = cv2.cvtColor(alqita, cv2.COLOR_BGR2RGB)
#obtain shape of image matrix:
shape = alqita.shape

#start by setting dowsample factor to 2
factor=2

#create output image as a numpy 3d 0's array:
output = np.zeros((int(shape[0]/factor),int(shape[1]/factor),3), dtype=np.uint8)



#print image dimentions:
print("Input image dimentions: ",shape)


#display original image:
plottool.imshow(alqita)
plottool.show()
#loop through to show 5 different scales:
for k in range(5):
    #print current dimensions:
    print("Current dimentions: ",output.shape[0], "x",output.shape[1])

    #currentPixel=image[0,0]
    for i in range(0,shape[0]-1,factor):
        for j in range(0,shape[1]-1,factor):
                output[int(i/factor),int(j/factor)]=alqita[i,j]
    
    #show result of current downscale:
    plottool.imshow(output)
    plottool.show()     
    cv2.imwrite(f'output/sampling/downscale-{k+1}.jpg',output)
    #increaes downscale:
    factor=factor*2
    #reset output image:
    if(k!=4):
        output = np.zeros((int(shape[0]/factor),int(shape[1]/factor),3), dtype=np.uint8)

#now we upscale the image in the same fashon as before:
print("---end of downsampling, begining of upsampling---")

#save final downsampled image as new starting image
alqita = output.copy()

#reset variables
shape = alqita.shape
factor=2
output = np.zeros((int(shape[0]*factor),int(shape[1]*factor),3), dtype=np.uint8)

for k in range(5):
    #print current dimensions:
    print("Current resolution: ",output.shape[0], "x",output.shape[1])

    #currentPixel=image[0,0]
    for i in range(0,shape[0]*factor,1):
        for j in range(0,shape[1]*factor,1):
                output[i,j]=alqita[int(i/factor),int(j/factor)]
    
    #show result of current upscale:
    plottool.imshow(output)
    plottool.show()     
    cv2.imwrite(f'output/sampling/upscale-{k+1}.jpg',output)
    #increaes upscale:
    factor=factor*2
    #reset output image:
    if(k!=4):
        output = np.zeros((int(shape[0]*factor),int(shape[1]*factor),3), dtype=np.uint8)


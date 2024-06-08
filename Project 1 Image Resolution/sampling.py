# Michael Rizig
# Project 1: Digital Image Processing
# 001008703
# File 1: Sampling
# 6/4/2024

#nessessary imports:
from skimage import io
import matplotlib.pyplot as plottool
import numpy as np
import cv2

#read in image:
catImagePath = 'input/cat.jpg'
alqita = io.imread(catImagePath)

#obtain shape of image matrix:
shape = alqita.shape

#start by setting dowsample factor to 2
factor=2

#create output image as a numpy 3d 0's array:
xSampledImage = np.zeros((int(shape[0]/factor),int(shape[1]/factor),3), dtype=np.uint8)



#print image dimentions:
print("Input image dimentions: ",shape)


#display original image:
plottool.imshow(alqita)
plottool.show()
#loop through to show 5 different scales:
for k in range(5):
    #print current dimensions:
    print("Current dimentions: ",xSampledImage.shape[0], "x",xSampledImage.shape[1])

    #currentPixel=image[0,0]
    #iterating through the entire image
    for i in range(0,shape[0]-1,factor):
        for j in range(0,shape[1]-1,factor):
                # we are setting the output pixel to the given input pixel
                # we divide by the factor when accessing the output image becase the output image is smaller, so a 1:1 access would cause out of bounds exception
                xSampledImage[int(i/factor),int(j/factor)]=alqita[i,j]
    
    #show result of current downscale:
    plottool.imshow(xSampledImage)
    plottool.show()   
    #shift colors to rgb
    xSampledImage = cv2.cvtColor(xSampledImage, cv2.COLOR_BGR2RGB)    
    cv2.imwrite(f'output/sampling/downscale-{k+1}.jpg',xSampledImage)
    #increaes downscale:
    factor=factor*2
    #reset output image:
    if(k!=4):
        xSampledImage = np.zeros((int(shape[0]/factor),int(shape[1]/factor),3), dtype=np.uint8)

#now we upscale the image in the same fashon as before:
print("---end of downsampling, begining of upsampling---")

#save final downsampled image as new starting image
alqita = xSampledImage.copy()

#reset variables
shape = alqita.shape
factor=2
xSampledImage = np.zeros((int(shape[0]*factor),int(shape[1]*factor),3), dtype=np.uint8)

for k in range(5):
    #print current dimensions:
    print("Current resolution: ",xSampledImage.shape[0], "x",xSampledImage.shape[1])

    #currentPixel=image[0,0]
    # since we are upscaing, we need to mutliply the range by our factor to ensure our output image has the correct number of pixels
    for i in range(0,shape[0]*factor,1):
        for j in range(0,shape[1]*factor,1):
                # since we are making a smaller image bigger, we need to divide the equivalent pixel i and j value by the factor of incresae so we dont get a memory segmentation falut trying to acccess the image
                # convert each value to integer incase we have an input image that is not square and we get a float value after divison
                xSampledImage[i,j]=alqita[int(i/factor),int(j/factor)]
    
    #show result of current upscale:
    plottool.imshow(xSampledImage)
    plottool.show()   
    #shift colors to rgb
    #output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)  
    cv2.imwrite(f'output/sampling/upscale-{k+1}.jpg',xSampledImage)
    #increaes upscale:
    factor=factor*2
    #reset output image:
    if(k!=4):
        xSampledImage = np.zeros((int(shape[0]*factor),int(shape[1]*factor),3), dtype=np.uint8)


# Michael Rizig
# Project 1: Digital Image Processing
# 001008703
# File 3: Color Quantization
# 6/8/2024

# imports
from skimage import io
import matplotlib.pyplot as plottool
import cv2
# this function takes in desired bit count and a given pixels grey value from file 2
# we are repurposing it for this file to change color levels
def filter(bits, x):
 # base case: if pixel is being converted into binary, simply check and return 1 or 0
    if bits==1:
        if x>127:
            return 255
        return 0   
    val = 256 / 2**bits
    # by dividing current pixel by ratio of 256/levels and convering from float to integer, we are essentially taking the floor of that value
    # by multiplying it by the original value, we lose any deviation from a even multiple, giving us n=bits possible outputs, properly scaled
    # example: x=126; bits=4 
    # val = 256/16 = 16
    # this means we only have 16 possible values for greyscale, those being : 0,16,32,48,64,80,96,112,128,144 etc
    # because of this fact, we are mimicing an n-bit greyscale by only displaying 2**n grey levels
    # 126 / 16 = 7.875; convering to int, 7.875 = 7
    # finally multiplying by 16 gives us 112.
    return val * int(x*(1/val))

#grab inital image same way as files 1 and 2
path = 'input/cat.jpg'
baseImage = io.imread(path)

#show initial image
plottool.imshow(baseImage)
plottool.show()

#create output image
out = baseImage.copy()

#color shift if needed
#cv2.cvtColor(baseImage,cv2.COLOR_BGR2RGB)

#define a divisor vector to contain each level of colors we desire
divisor = [12,6,3]

#loop through colors
for k in range (0,3):
    #loop through image pixels
    for i in range(baseImage.shape[0]):
        for j in range(baseImage.shape[1]):
            #loop through each color channel
            for pixel in range(0,3):
                #update each channel to fit given number of colors for each (divisor/3 since we have 3 colors)
                out[i][j][pixel] = filter(divisor[k]/3,baseImage[i][j][pixel])
    print('Image color levels from ',divisor[k]*2, " to " , divisor[k])
    #plot image
    plottool.imshow(out)
    #display image
    plottool.show()
    #convert colors
    out = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)
    #save image with appropriate name
    cv2.imwrite(f'output/color/downcolor{divisor[k]}bits-{k}.jpg',out)
    # restore output image to original quality for next itteration
    out=baseImage.copy()
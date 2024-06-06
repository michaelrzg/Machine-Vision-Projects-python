# Michael Rizig
# Project 1: Digital Image Processing
# File 2: Quantization
# 6/6/2024

# imports
from skimage import io
import matplotlib.pyplot as plottool
import cv2

# this function takes in desired bit count and a given pixels grey value
# and returns a conversion into the passed in bitcount greyscale value
def filter(bits, x):
    # base case: if image is being converted into binary, simply check and return 1 or 0
    if bits==1:
        if x>127:
            return 255
        return 0
    # for every other case: divide 256 (starting value) by number of greyscale levels desired
    val = 256 / 2**bits
    # by dividing current pixel by ratio of 256/greyscale levels and convering from float to integer, we are essentially taking the floor of that value
    # by multiplying it by the original value, we lose any deviation from a even multiple, giving us n=bits possible outputs, properly scaled
    # example: x=126; bits=4 
    # val = 256/16 = 16
    # this means we only have 16 possible values for greyscale, those being : 0,16,32,48,64,80,96,112,128,144 etc
    # because of this fact, we are mimicing an n-bit greyscale by only displaying 2**n grey levels
    # 126 / 16 = 7.875; convering to int, 7.875 = 7
    # finally multiplying by 16 gives us 112.
    return val * int(x*(1/val))
    
# define path for image
path = 'apple.jpeg'
# read in image into memory
image = io.imread(path)
# convert image from brg to rgb
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# create output image
out = image.copy()
# display initial image
print("Initial image: ")
plottool.imshow(image)
plottool.show()

for divisor in range (7,0,-1):
    for k in range(0,image.shape[0]):
        for j in range(0, image.shape[1]):
            v = filter(divisor,int(image[k][j][0]))
            out[k][j] = [v,v,v]
    print("Image greyscaled down from ", divisor+1 , " bits to " , divisor, " bits: ")
    # display current image
    plottool.imshow(out)
    plottool.show()
    # save current image with unique name
    cv2.imwrite(f'greyscale{divisor}-bits.jpeg',out)
    # reset out image to original for next pass
    out = image.copy()
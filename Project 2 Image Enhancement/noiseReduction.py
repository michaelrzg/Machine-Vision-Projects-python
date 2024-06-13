# Michael Rizig
# Project 2: Image Enhancement
# 001008703
# File 4: Noise Reduction via Average Filtering & Median Filtering
# 6/12/2024

# import nessesary libs
import cv2
from skimage import io
import matplotlib.pyplot as plottool
import statistics

# below function defines the average filter, which takes in the coordinates x, y of the pixel value, and the size of the desired filter.
def averageFilter(x,y,size):
    #init a sum varible to 0
    s =0
    #loop through the filter size. Since we want the filter to be centered at our x,y we need to modify the range of our loop
    # by dividing the filter size by 2, then going to the left and right by the quotent, we are essentially centering the filter
    # ive done this by setting the range from -(size of filter)/2 to (size of filter)/2 +1, then taking floor of these values
    # for example , with filter size 3, we get range -1,2, meaning our filter will span:
    # [i-1,j-1] [i-1,j] [i-1,j+1]
    # [i,  j-1] [i,  j] [i,  j+1]
    # [i+1,j-1] [i+1,j] [i+1,j+1]
    for i in range(-int(size/2),int(size/2)+1):
       for j in range(-int(size/2),int(size/2)+1):
        #for each value we add its weight to the sum (all values share the same weight in this implementation)
        s+= padded[x+i][y+j][0] / size**2
    #finally return the average
    return s 

#below function defines the medianfilter, which take the same range of value
def medianFilter(x,y,size):
    # instead of a sum, we define a set for all values
    s =[]
    
    #loop through the filter size. Since we want the filter to be centered at our x,y we need to modify the range of our loop
    # by dividing the filter size by 2, then going to the left and right by the quotent, we are essentially centering the filter
    # ive done this by setting the range from -(size of filter)/2 to (size of filter)/2 +1, then taking floor of these values
    # for example , with filter size 3, we get range -1,2, meaning our filter will span:
    # [i-1,j-1] [i-1,j] [i-1,j+1]
    # [i,  j-1] [i,  j] [i,  j+1]
    # [i+1,j-1] [i+1,j] [i+1,j+1]
    for i in range(-int(size/2),int(size/2)+1):
       for j in range(-int(size/2),int(size/2)+1):
        #instead of adding like we did before, we are simply appending each value to the list
        s.append( padded[x+i][y+j][0])
    
    #sort the values (the easy way)
    s.sort()
    #and finally return the median of the values
    return statistics.median(s)

#define filter sizes 
filter_size = [3,5,7]
# define image path
noisyAtriumPath = 'input/noisy_atrium.png'
# import image using skimage
noisyAtrium = io.imread(noisyAtriumPath)
#adjust colors from bgr to rgb
noisyAtrium = cv2.cvtColor(noisyAtrium,cv2.COLOR_BGR2RGB)

#print(noisyAtrium.shape)

#display original image
plottool.imshow(noisyAtrium)
plottool.show()

#this loop applies the average noise filter
for i in filter_size:
    
    #start by padding the image, which is one simple way described in the lectures to avoid out of bounds errors
    #padding by the floor of half the filter size: since center of filter is always an image pixel, we only need 1/2 of filter size out each direction
    padding = int(i/2)
    # use cv2 built in tool to add padding
    padded = cv2.copyMakeBorder(noisyAtrium,padding,padding,padding,padding,cv2.BORDER_CONSTANT,value=[0,0,0])
    # finally, initialize out output image for this filter
    out = padded.copy()
    
    #this loop goes through each pixle and applies the filter
    for k in range (padding,noisyAtrium.shape[0]-padding):
        for j in range(padding,noisyAtrium.shape[1]-padding):
            out[k][j] = averageFilter(k,j,i)           
    
    #save the image with the appropriate informative name
    cv2.imwrite(f'output/reduction/average/filtersize-{i}.png',out)
    
    #finally show each image and how the filter smoothing effected it
    plottool.imshow(out)
    plottool.show()        

# this loop works essentially the same way but with the median filtering
for i in filter_size:
    
    #create padding for image
    padding = int(i/2)
    padded = cv2.copyMakeBorder(noisyAtrium,padding,padding,padding,padding,cv2.BORDER_CONSTANT,value=[0,0,0])
    out = padded.copy() 
    
    #apply filter
    for k in range (padding,noisyAtrium.shape[0]-padding):
        for j in range(padding,noisyAtrium.shape[1]-padding):
            out[k][j] = medianFilter(k,j,i)
    #save and display        
    cv2.imwrite(f'output/reduction/median/filtersize-{i}.png',out)
    plottool.imshow(out)
    plottool.show()  
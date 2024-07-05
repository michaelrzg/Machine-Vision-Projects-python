# Michael Rizig
# Project 3: Morphological Filers
# 001008703
# File 1: Sharpening
# 7/5/2024

#Import nessessary tools
import matplotlib.pyplot as plottool
import cv2
from skimage import io

# below function defines the which is the sharpening filter used 
def lapician(x,y,size=3):
    #init a sum varible to 0
    s =0 
    c=0
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

path = 'input/moon.jpg'
moonimage = io.imread(path)
moonimage = cv2.cvtColor(moonimage,cv2.COLOR_BGR2RGB)
padded = cv2.copyMakeBorder(moonimage,1,1,1,1,cv2.BORDER_CONSTANT,value=[0,0,0])

output = moonimage.copy()

plottool.imshow(padded)
plottool.show()

for i in range(moonimage.shape[0]):
   for j in range(moonimage.shape[1]):
        output[i][j] =  output[i][j] + lapician(i,j) 
   
plottool.imshow(output)
plottool.show()
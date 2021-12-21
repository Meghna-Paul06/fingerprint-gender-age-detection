import cv2
from PIL import Image
def centerFp(i):
    img = cv2.imread(i)
    #img= Image.open(i)
 
# convert the image to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# convert the grayscale image to binary image
    ret,thresh = cv2.threshold(gray_image,127,255,0)
 
    M = cv2.moments(thresh)
# calculate x,y coordinate of center
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    return(cX,cY)

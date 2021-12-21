import cv2
import array
import scipy
import matplotlib
import matplotlib.pyplot as plt
import PIL
import numpy as np
import skimage.morphology
import skimage
import array
import math

from contrast import contrastStretching;
from noiser import noiseRemoval;
from binary import binaryConversion;
from getTerminationBifurcation import getTerminationBifurcation;
from removeSpuriousMinutiae import removeSpuriousMinutiae;
from center import centerFp;
#if __name__ == "__main__":
def main(i):
    arr1=[]
    arr2=[]
    contrastStretching(i)
    noiseRemoval()
    binaryConversion()
    x,y=centerFp(i);
    
    img = cv2.imread(i,0);
    img = np.uint8(img>128);
    
    skel = skimage.morphology.skeletonize(img)
    skel = np.uint8(skel)*255;
    
    mask = img*255;
    (minutiaeTerm, minutiaeBif, ridge, bifur,arr1,arr2) = getTerminationBifurcation(skel, mask);
    
    #print('Before removing spurious minutiae: ridge= ',ridge);
    #print('bifur= ',bifur);
    #print(arr)
    minutiaeTerm = skimage.measure.label(minutiaeTerm, 8);
    RP = skimage.measure.regionprops(minutiaeTerm)
    minutiaeTerm = removeSpuriousMinutiae(RP, np.uint8(img), 10);
    
    BifLabel = skimage.measure.label(minutiaeBif, 8);
    TermLabel = skimage.measure.label(minutiaeTerm, 8);
    
    minutiaeBif = minutiaeBif * 0;
    minutiaeTerm = minutiaeTerm * 0;
    
    (rows, cols) = skel.shape
    DispImg = np.zeros((rows,cols,3), np.uint8)
    DispImg[:,:,0] = skel; DispImg[:,:,1] = skel; DispImg[:,:,2] = skel;
        
    RP = skimage.measure.regionprops(BifLabel)
    for i in RP:
        (row, col) = np.int16(np.round(i['Centroid']))
        minutiaeBif[row, col] = 1;
        (rr, cc) = skimage.draw.circle_perimeter(row, col, 3);
        skimage.draw.set_color(DispImg, (rr,cc), (255,0,0));
   
    RP = skimage.measure.regionprops(TermLabel)
    for i in RP:
        (row, col) = np.int16(np.round(i['Centroid']))
        minutiaeTerm[row, col] = 1;
        (rr, cc) = skimage.draw.circle_perimeter(row, col, 3);
        skimage.draw.set_color(DispImg, (rr,cc), (0, 0, 255));
    cv2.imwrite('minutiae.png',DispImg)
    img = cv2.imread('minutiae.png',0);
    img = np.uint8(img>128);
    
    skel = skimage.morphology.skeletonize(img)
    skel = np.uint8(skel)*255;
    mask = img*255;    
    (minutiaeTerm, minutiaeBif, ridge1, bifur1,arr1,arr2) = getTerminationBifurcation(skel, mask);
    #print('After removing spurious minutiae: ridge= ',ridge1,' valley= ',ridge1-1);
    #print('bifur= ',bifur1);
    l=len(arr1)#no of ridge terminals
    s=0
    for i in range(0,l):
        for j in range(1,l):
            dist=round((math.sqrt(math.pow((arr1[i][0]-arr1[j][0]),2)+math.pow((arr1[i][1]-arr1[j][1]),2))),3)
            s=s+dist
        s=round((s/l),3)
    c=0;
    s1=0
    s2=0
    dist1=array.array('i')
    dist2=array.array('i')
    ridgearray=[]
    bifurarray=[]
    while c<120:
        d1=(int)(math.sqrt(math.pow((x-arr1[c][0]),2)+math.pow((y-arr1[c][1]),2)))
        dist1.append(d1);#ridge dist
        ob1=[d1,arr1[c][0],arr1[c][1]] #dist with pixel coordinates of ridge
        ridgearray.append(ob1)
        s1=s1+d1
        d2=(int)(math.sqrt(math.pow((x-arr2[c][0]),2)+math.pow((y-arr2[c][1]),2)))
        dist2.append(d2);#bifur dist
        ob2=[d2,arr2[c][0],arr2[c][1]]#dist with pixel coordinates of bifur
        bifurarray.append(ob2)
        s2=s2+d2
        c=c+1
    ridgearray.sort()
    bifurarray.sort()
    #print('Avg ridge dist= ',round(s1/200),' Avg bifur dist=',round(s2/200))
    return(dist1,dist2,ridgearray,bifurarray,s,x,y)

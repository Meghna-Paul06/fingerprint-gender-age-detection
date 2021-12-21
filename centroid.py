import csv
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pylab
import time
from main import main;
def centroid(i):
        #xc,yc=[],[]
        (x1,x2,ridge,bifur,inter,core_x,core_y) = main(i)  
        x,y=[],[]

        for i in range(0,120):
                x.append(x1[i])
                y.append(x2[i])
        x=np.array(x)
        y=np.array(y)

        x_len=len(x)
        y_len=len(y)

	#Set sum of points equal to x_sum and y_sum
        x_sum=np.sum(x)
        y_sum=np.sum(y)

	#Calculate centroid of points
        xc=x_sum/x_len
        yc=y_sum/y_len
        #print(ridge)
        #print(bifur)
        ridge.sort(reverse=True)
        bifur.sort(reverse=True)
        slope1=round(math.degrees(math.atan((core_y-ridge[0][2])/(core_x-ridge[0][1]))),3)
        slope2=round(math.degrees(math.atan((core_y-bifur[0][2])/(core_x-ridge[0][2]))),3)
        if slope1<0:
                slope1=360+slope1
        if slope2<0:
                slope2=360+slope2
     #   print('ridge= ',slope1)
       # print('bifur= ',slope2)
        #xc.append(x_centroid)
        #yc.append(y_centroid)

        #fig = plt.figure()
        fig = plt.figure(frameon=False)
        ax1 = fig.add_subplot(111)
#plt.plot(x,y,'+')
        ax1.scatter(x[:120],y[:120], c='b', marker="s", label='occurences')
        ax1.scatter(xc,yc, c='r', marker="o", label='centroid')
        plt.legend(loc='upper left')
        plt.xlabel('Ridge terminals')
        plt.ylabel('Bifurcation points')
        #ax1.arrow(ridge[0][1],ridge[0][2],xc-ridge[0][1],yc-ridge[0][2],width=0.02,color='red',head_length=0.0,head_width=0.0)
        #ax1.arrow(A[2][0],A[2][1],A[9][0]-A[2][0],A[9][1]-A[2][1],width=0.02,color='red',head_length=0.0,head_width=0.0)
        #print(round(x_centroid),round(y_centroid))
        plt.savefig("plot.png")
        plt.close("all")
            #d = ax1.collections[0]
        #d.set_offset_position('data')
        #arr=d.get_offsets()
        #print(arr)
        #np.asarray(arr)
        #print(arr[1][0],arr[1][1])
        return(xc,yc,inter,slope1,slope2)
        

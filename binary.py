import cv2
import numpy as np
from matplotlib import pyplot as plt
def binaryConversion():

    img = cv2.imread('img.png',0)
    img = cv2.medianBlur(img,5)

    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,11,2)
    fig = plt.figure(frameon=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.imshow(th2,'gray',vmin=0, vmax=30)
    plt.savefig("img.png", aspect='normal', bbox_inches='tight', pad_inches=0)
    return "img.png"

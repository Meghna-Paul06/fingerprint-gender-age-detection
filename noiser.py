import numpy as np
import cv2
from matplotlib import pyplot as plt

def noiseRemoval():
    img = cv2.imread('img.png')
    dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    fig = plt.figure(frameon=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.imshow(dst,vmin=0, vmax=30)
    plt.savefig("img.png", aspect='normal', bbox_inches='tight', pad_inches=0)
    return "img.png"

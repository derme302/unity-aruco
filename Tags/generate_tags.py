import cv2 as cv
import numpy as np
import cv2 as cv
import PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
print("OpenCV Version: " + cv.__version__)


aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)

fig = plt.figure()
nx = 4
ny = 3
for i in range(1, nx*ny+1):
    ax = fig.add_subplot(ny,nx,i)
    img = aruco.drawMarker(aruco_dict,i,700)
    plt.imshow(img, cmap = mpl.cm.gray, interpolation = "nearest")
    ax.axis("off")

plt.savefig("markers.pdf")
plt.show()

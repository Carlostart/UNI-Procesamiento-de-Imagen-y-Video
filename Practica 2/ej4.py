import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('spine_grises.tif',0)
plt.subplot(1,2,1)
plt.imshow(img,'gray')
plt.subplot(1,2,2)
plt.hist(img.ravel(),256,[0,255])
plt.show()

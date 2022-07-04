import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('rice.tif',0)
retval, threshold = cv2.threshold(img, 105, 255, cv2.THRESH_BINARY)
plt.imshow(threshold,'gray')
plt.show()
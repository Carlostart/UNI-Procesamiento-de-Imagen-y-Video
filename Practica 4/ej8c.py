import cv2
import matplotlib.pyplot as plt
import numpy as np
import convolucion as cnv

img = cv2.imread('WAFER1.TIF',0)
img_gaussian = cv2.GaussianBlur(img,(3,3),0)

vertical = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

J = cnv.convolucion(img_gaussian,vertical)

abs = np.absolute(J)

plt.imshow(abs,'gray')
plt.title('bordes verticales')
plt.yticks([])
plt.xticks([])

plt.show()
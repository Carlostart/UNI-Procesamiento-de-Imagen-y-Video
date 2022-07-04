import cv2
import matplotlib.pyplot as plt
import numpy as np
import convolucion as cnv

img = cv2.imread('BUG.TIF', 0)

gh = np.array([[1, 1, 1], [0, 1, 0], [-1, -1, -1]])

conv = cnv.convolucion(img,gh)
hor = np.absolute(conv)
h, w = hor.shape
for i in range(h):
    for j in range(w):
        if hor[i,j]>255:
            hor[i,j]=255

plt.imshow(hor, 'gray')
plt.title('horizontal')
plt.xticks([])
plt.yticks([])

plt.show()

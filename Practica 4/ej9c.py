import cv2
import matplotlib.pyplot as plt
import numpy as np
import convolucion as cnv

img = cv2.imread('coins.png',0)

gv = np.array([[-1, 0, 1], [-1, 1, 1], [-1, 0, 1]])
gh = np.array([[1, 1, 1], [0, 1, 0], [-1, -1, -1]])

Jv = np.absolute(cnv.convolucion(img,gv))/255
Jh = np.absolute(cnv.convolucion(img,gh))/255

plt.subplot(1,2,1)
plt.imshow(Jv,'gray')
plt.title('vertical')
plt.xticks([])
plt.yticks([])

plt.subplot(1,2,2)
plt.imshow(Jh, 'gray')
plt.title('horizontal')
plt.xticks([])
plt.yticks([])

plt.show()

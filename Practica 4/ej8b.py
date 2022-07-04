import cv2
import matplotlib.pyplot as plt
import numpy as np
import convolucion as cnv

img = cv2.imread('rice.tif', 0)
img_gaussian = cv2.GaussianBlur(img, (3, 3), 0)

horizontal=np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
vertical = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
H = cnv.convolucion(img_gaussian, horizontal)
V = cnv.convolucion(img_gaussian, vertical)
R = H+V

umbral = 55
retval, H = cv2.threshold(np.absolute(H),umbral,255,cv2.THRESH_BINARY)
retval, V = cv2.threshold(np.absolute(V),umbral,255,cv2.THRESH_BINARY)
retval, R = cv2.threshold(np.absolute(R),umbral,255,cv2.THRESH_BINARY)

plt.subplot(131)
plt.imshow(H,'gray')
plt.title('bordes horizontales')
plt.xticks([])
plt.yticks([])

plt.subplot(132)
plt.imshow(V,'gray')
plt.title('bordes verticales')
plt.xticks([])
plt.yticks([])

plt.subplot(133)
plt.imshow(R,'gray')
plt.title('ambos')
plt.xticks([])
plt.yticks([])

plt.show()

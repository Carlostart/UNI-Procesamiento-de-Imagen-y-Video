import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('BRAIN_RT.TIF',0)
f = np.fft.fft2(img)
f1 = np.fft.fftshift(f)
plt.subplot(121),plt.imshow(img, 'gray')
plt.title('Imagen de entrada'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(np.log(np.abs(f1)),'jet')
plt.title('FFT'), plt.xticks([]), plt.yticks([]), plt.colorbar();
plt.show()
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('saturno.tif',0)

img_gaussian = cv2.GaussianBlur(img,(3,3),0)

lap = cv2.Laplacian(img_gaussian, cv2.CV_64F)

sharp = img_gaussian - 0.7*lap

plt.imshow(lap, 'gray')
plt.title('sharpened')
plt.xticks([])
plt.yticks([])
plt.show()


import cv2
import matplotlib.pyplot as plt

img = cv2.imread('BRAIN_RT.TIF',0)
img = cv2.equalizeHist(img)

plt.subplot(1,3,1)
plt.imshow(img, 'gray')
plt.title('histeq')
plt.xticks([])
plt.yticks([])

canny = cv2.Canny(img,100,200)

plt.subplot(1,3,2)
plt.imshow(canny, 'gray')
plt.title('Canny')
plt.xticks([])
plt.yticks([])

R = img/255+0.1*canny/255

plt.subplot(1,3,3)
plt.imshow(R,'gray')
plt.title('realzada')
plt.xticks([])
plt.yticks([])
plt.show()

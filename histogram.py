import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('lenata.pgm',0)
cv.imshow('Lena',img)
plt.hist(img.ravel(),256,[0,256]); 
plt.show()

cv.waitKey(0)  
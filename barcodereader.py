
import numpy as np
import cv2 as cv
from pyzbar import pyzbar

img = cv.imread('/home/mio/Documents/Barcode/images/Untitled.jpg', cv.IMREAD_GRAYSCALE)
img = cv.resize(img , (img.shape[1]*2,img.shape[0]*2))
closed = cv.morphologyEx(img, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_RECT, (1, 2)))
cv.imshow("closed",closed)
cv.waitKey(0)

print(img.shape)
dens = np.sum(img, axis=0)
mean = np.mean(dens)
print(mean)

thresh = closed.copy()
for idx, val in enumerate(dens):
    if val< 10800:
        thresh[:,idx] = 0
(_, thresh2) = cv.threshold(thresh, 150, 255, cv.THRESH_BINARY )
cv.imshow("closed",thresh2)
cv.waitKey(0)
barcodes = pyzbar.decode(thresh2)
print(barcodes[0].data)

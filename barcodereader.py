# from PIL import Image
# from pyzbar.pyzbar import decode, ZBarSymbol
# import cv2
# import numpy as np


# # Load the pre-trained super resolution model
# sr_model = cv2.dnn_superres.DnnSuperResImpl_create()
# sr_model.readModel("/home/mio/Documents/Barcode/export/ESPCN_x4.pb")
# sr_model.setModel("espcn", 4)

# # Read the input image
# image = cv2.imread("/home/mio/Documents/Barcode/images/1_1.jpg")
# x,y,h = image.shape
# # Print input image dimensions
# #========================
# # Import Libraies
# #========================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt 
from pyzbar import pyzbar

#------------------------
# Read Image
#========================
img = cv.imread('/home/mio/Documents/Barcode/images/1_1.jpg', cv.IMREAD_GRAYSCALE)
img = cv2.resize(img , (img.shape[1]*5,img.shape[0]*5))
# #------------------------
# # Morphology
# #========================
# # Closing
# #------------------------
closed = cv.morphologyEx(img, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_RECT, (1, 2)))
cv2.imshow("closed",closed)
cv2.waitKey(0)

# #------------------------
# # Statistics
# #========================
print(img.shape)
dens = np.sum(img, axis=0)
mean = np.mean(dens)
print(mean)

#------------------------
# Thresholding
#========================
thresh = closed.copy()
for idx, val in enumerate(dens):
    if val< 10800:
        thresh[:,idx] = 0

(_, thresh2) = cv.threshold(thresh, 150, 255, cv.THRESH_BINARY )
cv2.imshow("closed",thresh2)
cv2.waitKey(0)
# #------------------------
# # plotting the results
# #========================
# plt.figure(num='barcode')

# plt.subplot(221)
# plt.imshow(img, cmap='gray')
# plt.title('Original')
# plt.axis('off')

# plt.subplot(224)
# plt.imshow(thresh, cmap='gray')
# plt.title('Thresholded')
# plt.axis('off')

# plt.subplot(223)
# plt.imshow(thresh2, cmap='gray')
# plt.title('Result')
# plt.axis('off')

# plt.subplot(222)
# plt.hist(dens)
# plt.axvline(dens.mean(), color='k', linestyle='dashed', linewidth=1)
# plt.title('dens hist')

# plt.show()

# #------------------------
# # Printing the Output
# #========================
barcodes = pyzbar.decode(thresh2)
print(barcodes)

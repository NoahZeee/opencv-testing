import cv2 as cv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from IPython.display import Image

img = cv.imread('checkerboard_18x18.png')

# the '0' flag converts the image to grayscale
grayscale = cv.imread('checkerboard_18x18.png', 0)

# prints image array
# print(grayscale)


#print size of image
# print("Image size (H, W):", grayscale.shape)

#print datatype of image
# print("Image datatype:", grayscale.dtype)

coke_img = cv.imread("coca-cola-logo.png", 1)
# plt.imshow(coke_img)
# plt.savefig('coke_image.png')

# reverse the color channels from BGR to RGB
coke_img_reversed = coke_img[:, :, ::-1]
# plt.imshow(coke_img_reversed)
# plt.savefig('coke_image_reversed.png')

# Split the image into b, g, r, components
img_NZ_bgr = cv.imread("New_Zealand_Lake.jpg", cv.IMREAD_COLOR)
b, g, r = cv.split(img_NZ_bgr)

# # show channels
# plt.figure(figsize=(12, 8))

# plt.subplot(141);plt.imshow(r, cmap="gray");plt.title('Red Channel')
# plt.subplot(142);plt.imshow(g, cmap="gray");plt.title('Green Channel')
# plt.subplot(143);plt.imshow(b, cmap="gray");plt.title('Blue Channel')

# # Merge the individual channels back into a BGR image
# imgMerged = cv.merge((b, g, r))
# # show the output
# plt.subplot(144)
# plt.imshow(imgMerged[:, :, ::-1])
# plt.title("Merged Output")
# plt.savefig('NZ_Lake_Channels.png')
import cv2 as cv
import numpy as np
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

# print image size
print("image size (H, W, C):", coke_img.shape)
 
# ***** WHEN I COME BACK TO THIS - FIX MATPLOTLIB DISPLAY ISSUE ******
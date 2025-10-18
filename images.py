import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image

img = cv.imread('checkerboard_18x18.png')

# the '0' flag converts the image to grayscale
grayscale = cv.imread('checkerboard_18x18.png', 0)

print(grayscale)

Image(filename='checkerboard_18x18.png')
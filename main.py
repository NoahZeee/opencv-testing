import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image

img = cv.imread('checkerboard_180x180.png')
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.show()


import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import numpy as np
from PIL import Image
import cv2

img = cv2.imread("lenna.png")
h,w = img.shape[:2]
print(h,w)
imag_gray = np.zeros([h, w], img.dtype)
for i in range(h):
    for j in range(w):
        m = img[i, j]
        imag_gray[i, j] = int(m[0]*0.11 + m[1]*0.59 + m[2]*0.3)
print(m)
print(imag_gray)
print("image show gray: %s"%imag_gray)
cv2.imshow("image show gray",imag_gray)
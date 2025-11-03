import cv2
import numpy as np

img = cv2.imread('assets/tiger.jpg')
blue = img[:, :, 0]
green = img[:, :, 1]
red = img[:, :, 2]
gray = (0.114 * blue + 0.587 * green + 0.299 * red)
gray8bit = gray.astype(np.uint8)
threshold = 127
mask = gray8bit > threshold
binary_img = np.zeros_like(gray8bit)
binary_img[mask] = 255

cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', gray8bit)
cv2.imshow('Binary Image', binary_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

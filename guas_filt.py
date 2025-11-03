import cv2
import numpy as np

img = cv2.imread('assets/flower.jpg')
rows, cols, ch = img.shape
filtered_img = np.zeros_like(img, dtype=np.float32)

kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]], dtype=np.float32) / 16

for k in range(ch):
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            region = img[i - 1:i + 2, j - 1:j + 2, k]
            val = np.sum(region * kernel)
            filtered_img[i, j, k] = val

final_img = np.uint8(filtered_img)

cv2.imshow("Original img:", img)
cv2.imshow("filtered img:", final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

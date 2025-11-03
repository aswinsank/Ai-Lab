import cv2
import numpy as np

img = cv2.imread('assets/tiger1.jpg')
rows, cols, ch = img.shape
filtered_img = np.zeros_like(img, dtype=np.float32)

for k in range(ch):
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            region = img[i - 1:i + 2, j - 1:j + 2, k]
            avg = np.sum(region) / 9
            filtered_img[i, j, k] = avg

filtered_img = np.uint8(filtered_img)

cv2.imshow("Original", img)
cv2.imshow("3x3 Averaged (Color)", filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

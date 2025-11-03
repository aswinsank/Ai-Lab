import cv2
import numpy as np

img = cv2.imread('assets/flower.jpg')
rows, cols, ch = img.shape
filtered_img = np.zeros_like(img, dtype=np.float32)

for k in range(ch):
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            region = img[i - 1:i + 2, j - 1:j + 2, k]
            val = np.median(region)
            filtered_img[i, j, k] = val

final_img = np.uint8(filtered_img)

cv2.imshow("Original img:", img)
cv2.imshow("filtered img:", final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#5x5
for i in range(2, rows - 2):
    for j in range(2, cols - 2):
        region = img[i - 2:i + 3, j - 2:j + 3, k]
        val = np.median(region)
        filtered_img[i, j, k] = val
#7x7
for i in range(3, rows - 3):
    for j in range(3, cols - 3):
        region = img[i - 3:i + 4, j - 3:j + 4, k]
        val = np.median(region)
        filtered_img[i, j, k] = val

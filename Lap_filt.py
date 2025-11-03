import cv2
import numpy as np

img = cv2.imread('assets/tiger1.jpg')
rows, cols, ch = img.shape
filtered_img = np.zeros_like(img, dtype=np.float32)

kernel = np.array([[0, -1, 0],
                   [-1, 4, -1],
                   [0, -1, 0]], dtype=np.float32)

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

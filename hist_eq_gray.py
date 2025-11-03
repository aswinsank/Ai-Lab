import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the image in grayscale
img = cv2.imread('assets/tiger1.jpg', 0)   # 0 → grayscale mode
rows, cols = img.shape

# Step 2: Calculate Histogram (count of each intensity)
hist = [0] * 256
for i in range(rows):
    for j in range(cols):
        k = img[i, j]
        hist[k] += 1

# Step 3: Calculate PDF (Probability Distribution Function)
pdf = [h / (rows * cols) for h in hist]

# Step 4: Calculate CDF (Cumulative Distribution Function)
cdf = [0] * 256
cdf[0] = pdf[0]
for i in range(1, 256):
    cdf[i] = cdf[i - 1] + pdf[i]

# Step 5: Normalize CDF to 0–255 range
equalized_map = [round(c * 255) for c in cdf]

# Step 6: Apply the equalization mapping
equalized = np.zeros_like(img)
for i in range(rows):
    for j in range(cols):
        k = img[i, j]
        equalized[i, j] = equalized_map[k]

# Step 7: Display original and equalized images
cv2.imshow("Original Image", img)
cv2.imshow("Equalized Image", equalized)

# Step 8: Plot histograms
plt.hist(img.ravel(), bins=256, color='gray')
plt.title("Histogram before equalization")
plt.show()

plt.hist(equalized.ravel(), bins=256, color='gray')
plt.title("Histogram after equalization")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image in color
img = cv2.imread('assets/tiger1.jpg')

# Convert BGR → HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
rows, cols = v.shape

# Step 1: Compute histogram manually
hist = [0] * 256
for i in range(rows):
    for j in range(cols):
        k = v[i, j]
        hist[k] += 1

# Step 2: Compute PDF
pdf = [h / (rows * cols) for h in hist]

# Step 3: Compute CDF
cdf = [0] * 256
cdf[0] = pdf[0]
for i in range(1, 256):
    cdf[i] = cdf[i - 1] + pdf[i]

# Step 4: Normalize to 0–255
equalized_map = [round(c * 255) for c in cdf]

# Step 5: Apply mapping to V channel
v_eq = np.zeros_like(v)
for i in range(rows):
    for j in range(cols):
        k = v[i, j]
        v_eq[i, j] = equalized_map[k]

# Merge and convert back to BGR
hsv_eq = cv2.merge([h, s, v_eq])
img_eq = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Equalized Image", img_eq)

# Plot histograms for V channel
plt.hist(v.ravel(), bins=256)
plt.title("Histogram before equalization")
plt.show()

plt.hist(v_eq.ravel(), bins=256)
plt.title("Histogram after equalization")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

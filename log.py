import cv2
import numpy as np

# Step 1: Read the grayscale image
img = cv2.imread('assets/tigergrey.jpeg', cv2.IMREAD_GRAYSCALE)

# Step 2: Convert image to float for logarithmic operation
float_img = img.astype(np.float64)

# Step 3: Apply log transformation
# Formula: s = c * log(1 + r)
log_transformed = np.log1p(float_img)

# Step 4: Normalize result to 0–255
normalized_log = log_transformed / np.log1p(float_img.max())
log_img = np.uint8(255 * normalized_log)

# Step 5: Display original and log-transformed images
cv2.imshow("Original Image", img)
cv2.imshow("Log Transformed Image", log_img)

# Step 6: Wait for key press and close
cv2.waitKey(0)
cv2.destroyAllWindows()

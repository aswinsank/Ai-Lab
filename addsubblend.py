import cv2
import numpy as np

# Step 1: Read two images
img1 = cv2.imread('assets/tiger.jpeg')
img2 = cv2.imread('assets/cat.jpeg')

# Step 2: Resize both images to same dimensions
img1 = cv2.resize(img1, (200, 200))
img2 = cv2.resize(img2, (200, 200))

# Step 3: Perform image addition
added_img = cv2.add(img1, img2)

# Step 4: Perform image subtraction
subtracted_img = cv2.subtract(img1, img2)

# Step 5: Perform image blending
# Formula: result = (α * img1) + (β * img2) + γ
blended_img = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

# Step 6: Display all results
cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Added Image", added_img)
cv2.imshow("Subtracted Image", subtracted_img)
cv2.imshow("Blended Image", blended_img)

# Step 7: Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

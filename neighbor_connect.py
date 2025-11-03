import cv2
import numpy as np

# Step 1: Read the image in grayscale
img = cv2.imread('assets/neighbour.jpg', 0)

# Step 2: Convert to binary image (thresholding)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Step 3: Get image dimensions
rows, cols = binary.shape

# Step 4: Create empty arrays to store results
same_4_array = np.zeros((rows, cols), dtype=np.uint8)
same_8_array = np.zeros((rows, cols), dtype=np.uint8)

# Step 5: Define 4-connected and 8-connected neighbour coordinates
neighbours_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
neighbours_8 = neighbours_4 + [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Step 6: Loop through each pixel to count similar neighbours
for x in range(rows):
    for y in range(cols):
        curr = binary[x, y]
        same_4 = 0
        same_8 = 0

        # Check 4-connected neighbours
        for dx, dy in neighbours_4:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if curr == binary[nx, ny]:
                    same_4 += 1

        # Check 8-connected neighbours
        for dx, dy in neighbours_8:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if curr == binary[nx, ny]:
                    same_8 += 1

        same_4_array[x, y] = same_4
        same_8_array[x, y] = same_8

# Step 7: Display all images
cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", binary)
cv2.imshow("4-Neighbour Similarity", same_4_array)
cv2.imshow("8-Neighbour Similarity", same_8_array)

# Step 8: Wait for key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

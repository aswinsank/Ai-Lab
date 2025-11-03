import cv2
import numpy as np

# Step 1: Create two black images
img1 = np.zeros((200, 200), dtype=np.uint8)
img2 = np.zeros((200, 200), dtype=np.uint8)

# Step 2: Draw white shapes on them
cv2.rectangle(img1, (50, 50), (150, 150), 255, -1)   # White square
cv2.circle(img2, (100, 100), 60, 255, -1)            # White circle

# Step 3: Perform bitwise operations
bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_xor = cv2.bitwise_xor(img1, img2)

# Step 4: Display all images
cv2.imshow("Image 1 (Rectangle)", img1)
cv2.imshow("Image 2 (Circle)", img2)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise XOR", bitwise_xor)

# Step 5: Wait for key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

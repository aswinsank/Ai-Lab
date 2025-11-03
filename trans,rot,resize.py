import cv2
import numpy as np

# Load the image
img = cv2.imread(r'D:\ai-lab\assets\tiger.jpg')


# Translation (move)
tx, ty = 100, 50
rows, cols = img.shape[:2]
trans_mat = np.float32([[1, 0, tx], [0, 1, ty]])
trans_img = cv2.warpAffine(img, trans_mat, (cols, rows))

# Scaling (resize)
scaled_img = cv2.resize(img, None, fx=0.5, fy=0.5)

# Rotation (45 degrees)
angle = 45
rot_mat = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
rot_img = cv2.warpAffine(img, rot_mat, (cols, rows))

# Rotation (90 degrees)
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Display all images
cv2.imshow("Original", img)
cv2.imshow("Translated", trans_img)
cv2.imshow("Resized", scaled_img)
cv2.imshow("Rotation_45", rot_img)
cv2.imshow("Rotation_90", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()

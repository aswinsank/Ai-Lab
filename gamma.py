import cv2
import numpy as np

# Function for gamma correction
def gamma_correction(img, gamma):
    # Step 1: Normalize pixel values to [0,1]
    img_normalized = img / 255.0

    # Step 2: Apply gamma correction
    gamma_applied = np.power(img_normalized, gamma)

    # Step 3: Scale back to [0,255]
    gamma_img = np.uint8(gamma_applied * 255)

    return gamma_img


# Step 4: Read grayscale and color images
gray = cv2.imread('assets/tigergrey.jpeg', 0)
color = cv2.imread('assets/tiger.jpeg')

# Step 5: Define list of gamma values
gammas = [0.2, 0.5, 1.5, 2, 3]

# Step 6: Apply gamma correction for each gamma value
for g in gammas:
    corrected_gray = gamma_correction(gray, g)
    corrected_color = gamma_correction(color, g)

    cv2.imshow(f"Gamma {g} (Gray)", corrected_gray)
    cv2.imshow(f"Gamma {g} (Color)", corrected_color)

# Step 7: Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()

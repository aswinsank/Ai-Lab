import cv2
import numpy as np

# Function to create and display image negative
def image_negative(image_path):
    # Step 1: Read the image
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # Step 2: Check if image is grayscale or color
    if len(img.shape) == 2:
        # Grayscale or binary image
        neg = 255 - img
    else:
        # Color image: process each channel separately
        b, g, r = cv2.split(img)
        b_neg = 255 - b
        g_neg = 255 - g
        r_neg = 255 - r
        neg = cv2.merge([b_neg, g_neg, r_neg])

    # Step 3: Display original and negative images
    cv2.imshow("Original Image", img)
    cv2.imshow("Negative Image", neg)

    # Step 4: Wait for key press and close
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Step 5: Test the function with different images
colorimage = 'assets/binaryimage.jpg'
greyimage = 'assets/tigergrey.jpeg'
binaryimage = 'assets/tiger.jpg'

image_negative(colorimage)
image_negative(greyimage)
image_negative(binaryimage)

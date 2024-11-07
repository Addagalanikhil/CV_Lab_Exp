import cv2
import numpy as np

# Read the image from the specified path
img = cv2.imread(r"C:\Users\nikhi\Downloads\allcv.png")

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not read the image.")
    exit()

# Get the dimensions of the image
(h, w) = img.shape[:2]

# Define the points for the perspective transformation
# Source points (corners of the region to be transformed)
src_points = np.float32([[100, 100], [300, 100], [100, 300], [300, 300]])

# Destination points (where the corners will be mapped)
dst_points = np.float32([[50, 50], [350, 50], [50, 350], [350, 350]])

# Get the perspective transformation matrix
perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# Perform the perspective transformation
transformed_img = cv2.warpPerspective(img, perspective_matrix, (w, h))

# Display the original and transformed images
cv2.imshow("Original Image", img)
cv2.imshow("Transformed Image (Perspective)", transformed_img)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

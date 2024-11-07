import cv2
import numpy as np

# Define the kernel for dilation and erosion
kernel = np.ones((5, 5), np.uint8)
print("Kernel:\n", kernel)

# Define the path to the image and load it
path = r"C:\Users\nikhi\Downloads\allcv.png"
img = cv2.imread(path)

# Check if the image loaded successfully
if img is None:
    print("Error: Could not read the image. Please check the file path.")
else:
    # Convert the image to grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian Blur to reduce noise
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
    
    # Perform edge detection using Canny
    imgCanny = cv2.Canny(imgBlur, 100, 200)
    
    # Dilate the edges to make them more prominent
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=2)
    
    # Optional: Erode the dilated image slightly to reduce thickness
    imgEroded = cv2.erode(imgDilation, kernel, iterations=1)
    
    # Display the eroded image
    cv2.imshow("Image Erosion", imgEroded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

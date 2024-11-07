import cv2
import numpy as np

def modify_roi(image_path):
    # Step 1: Load the image
    img = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if img is None:
        print("Error: Could not read the image.")
        return

    # Step 2: Define the ROI coordinates (x, y, width, height)
    # For example, let's define a rectangle at (50, 50) with a width and height of 200 pixels
    x, y, w, h = 50, 50, 200, 200

    # Step 3: Extract the ROI
    roi = img[y:y+h, x:x+w]

    # Step 4: Modify the ROI (fill it with a solid color, e.g., red)
    # Create a solid color image (BGR format)
    color_fill = np.zeros(roi.shape, dtype=np.uint8)
    color_fill[:] = [0, 0, 255]  # Red color in BGR

    # Fill the ROI with the red color
    img[y:y+h, x:x+w] = color_fill

    # Step 5: Display the modified image
    cv2.imshow("Modified Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    image_path = r"C:\Users\GOUSE\OneDrive\Pictures\Camera Roll\WhatsApp Image 2024-11-06 at 13.03.24_9838cc31.jpg"
    modify_roi(image_path)

import cv2
import numpy as np

def apply_smoothing_filter(image_path, kernel_size=5):
    """
    Applies a smoothing (averaging) filter to an image using OpenCV.

    Parameters:
    - image_path: str, path to the input image.
    - kernel_size: int, size of the kernel (must be odd and greater than 1).
    """
    # Step 1: Load the image
    img = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if img is None:
        print("Error: Could not read the image.")
        return

    # Step 2: Apply the averaging filter
    # Ensure kernel size is odd and greater than 1
    if kernel_size % 2 == 0 or kernel_size < 1:
        print("Kernel size must be an odd number greater than 1.")
        return

    # Apply the averaging filter
    smoothed_img = cv2.blur(img, (kernel_size, kernel_size))

    # Step 3: Display the original and smoothed images
    cv2.imshow("Original Image", img)
    cv2.imshow("Smoothed Image", smoothed_img)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    image_path = r"C:\Users\nikhi\Downloads\allcv.png"
    apply_smoothing_filter(image_path, kernel_size=5)

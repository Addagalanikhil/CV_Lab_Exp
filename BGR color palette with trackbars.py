import cv2
import numpy as np

def bgr_color_palette():
    """
    Creates a BGR color palette using OpenCV trackbars to adjust the color values.
    """
    # Create a window
    cv2.namedWindow("BGR Color Palette")

    # Initialize BGR values
    b, g, r = 0, 0, 0

    # Create trackbars for BGR values
    cv2.createTrackbar("Blue", "BGR Color Palette", 0, 255, lambda x: None)
    cv2.createTrackbar("Green", "BGR Color Palette", 0, 255, lambda x: None)
    cv2.createTrackbar("Red", "BGR Color Palette", 0, 255, lambda x: None)

    while True:
        # Get the current positions of the trackbars
        b = cv2.getTrackbarPos("Blue", "BGR Color Palette")
        g = cv2.getTrackbarPos("Green", "BGR Color Palette")
        r = cv2.getTrackbarPos("Red", "BGR Color Palette")

        # Create an image filled with the selected color
        color_image = np.zeros((300, 600, 3), dtype=np.uint8)
        color_image[:] = [b, g, r]  # OpenCV uses BGR format

        # Display the color image
        cv2.imshow("BGR Color Palette", color_image)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Destroy all windows
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    bgr_color_palette()

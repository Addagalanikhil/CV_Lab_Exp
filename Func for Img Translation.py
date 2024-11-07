import cv2
import numpy as np

def translate_image(image_path, tx, ty):
    """
    Translates (shifts) an image by specified x and y offsets.

    Parameters:
    - image_path: str, path to the input image.
    - tx: int, translation in the x direction (positive to the right, negative to the left).
    - ty: int, translation in the y direction (positive downwards, negative upwards).
    """
    # Step 1: Load the image
    img = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if img is None:
        print("Error: Could not read the image.")
        return

    # Step 2: Define the translation matrix
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

    # Step 3: Apply the translation
    translated_img = cv2.warpAffine(img, translation_matrix, (img.shape[1], img.shape[0]))

    # Step 4: Display the original and translated images
    cv2.imshow("Original Image", img)
    cv2.imshow("Translated Image", translated_img)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    image_path = r"C:\Users\nikhi\Downloads\allcv.png"
    translate_image(image_path, tx=50, ty=30)  # Translate right by 50 pixels and down by 30 pixels

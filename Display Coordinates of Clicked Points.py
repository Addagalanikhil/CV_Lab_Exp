import cv2

# List to store clicked points
clicked_points = []

def click_event(event, x, y, flags, param):
    """
    Mouse callback function to capture click events and store coordinates.

    Parameters:
    - event: The event type (e.g., mouse click).
    - x: The x-coordinate of the mouse click.
    - y: The y-coordinate of the mouse click.
    - flags: Any relevant flags (not used here).
    - param: Additional parameters (not used here).
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        # Store the coordinates of the clicked point
        clicked_points.append((x, y))
        # Print the coordinates to the console
        print(f"Point clicked: ({x}, {y})")
        # Draw a circle at the clicked point
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)  # Green circle
        # Display the coordinates on the image
        cv2.putText(img, f"({x}, {y})", (x + 10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Show the updated image
        cv2.imshow("Image", img)

def display_coordinates(image_path):
    """
    Displays an image and captures the coordinates of points clicked on it.

    Parameters:
    - image_path: str, path to the input image.
    """
    global img
    # Read the image
    img = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if img is None:
        print("Error: Could not read the image.")
        return

    # Create a window and set the mouse callback function
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", click_event)

    while True:
        # Display the image
        cv2.imshow("Image", img)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Destroy all windows
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    image_path = r"C:\Users\nikhi\Downloads\allcv.png"
    display_coordinates(image_path)

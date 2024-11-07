import cv2

# Define the video path and create a VideoCapture object
cap = cv2.VideoCapture(r"C:\Users\nikhi\Downloads\cv-video.mp4")

# Check if the video opened successfully
if not cap.isOpened():
    print("Error opening video file")
else:
    # Set playback speed using keywords
    playback_mode = "fast"  # Set to "slow" or "fast"

    # Define playback speeds in milliseconds
    playback_speed = 100 if playback_mode == "slow" else 10

    # Display video frames
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Frame', frame)

            # Exit if 'q' is pressed
            if cv2.waitKey(playback_speed) & 0xFF == ord('q'):
                break
        else:
            break

    # Release video and close windows
    cap.release()
    cv2.destroyAllWindows()

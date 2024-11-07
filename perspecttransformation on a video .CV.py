import cv2
import numpy as np

# Path to the input video
video_path = r"C:\Users\GOUSE\OneDrive\Desktop\opencvApp\fast clip.mp4"
output_path = r"C:\Users\GOUSE\OneDrive\Desktop\opencvApp\transformed_video.mp4"

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get the width and height of the video frames
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the source points for the perspective transformation
src_points = np.float32([[100, 100], [frame_width - 100, 100], [100, frame_height - 100], [frame_width - 100, frame_height - 100]])

# Define the destination points for the perspective transformation
dst_points = np.float32([[50, 50], [frame_width - 50, 50], [50, frame_height - 50], [frame_width - 50, frame_height - 50]])

# Get the perspective transformation matrix
perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
out = cv2.VideoWriter(output_path, fourcc, 30.0, (frame_width, frame_height))

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    
    # Break the loop if there are no more frames
    if not ret:
        break
    
    # Perform the perspective transformation on the frame
    transformed_frame = cv2.warpPerspective(frame, perspective_matrix, (frame_width, frame_height))
    
    # Write the transformed frame to the output video
    out.write(transformed_frame)

    # Optionally display the transformed frame
    cv2.imshow("Transformed Frame", transformed_frame)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and writer objects
cap.release()
out.release()
cv2.destroyAllWindows()

import cv2
import numpy as np
kernel = np.ones((5, 5), np.uint8)
print(kernel)
path = r"C:\Users\nikhi\Downloads\allcv.png"
img = cv2.imread(path)
if img is None:
    print("Error: Could not read the image. Please check the file path.")
else:
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    cv2.imshow("GrayScale", imgGray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

import cv2 
import numpy as np 
kernel = np.ones((5,5),np.uint8) 
img = cv2.imread(r"C:\Users\nikhi\Downloads\allcv.png",cv2.IMREAD_COLOR) 
img = cv2.resize(img,(150,150)) 
cv2.imshow("image",img) 
cv2.waitKey(0) 

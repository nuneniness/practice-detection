import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of pringles color in HSV
    lower_y = np.array([18, 120, 120], dtype=np.uint8)
    upper_y = np.array([38, 255,255], dtype=np.uint8)
    lower_b = np.array([-10, 100, 100], dtype=np.uint8)
    upper_b = np.array([10, 255,255], dtype=np.uint8)

    # Threshold the HSV image
    mask_y = cv2.inRange(hsv, lower_y, upper_y)
    mask_b = cv2.inRange(hsv, lower_b, upper_b)
    mask = mask_y + mask_b

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

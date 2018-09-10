#!/usr/bin/python2.7
import cv2
import numpy as np

img = cv2.imread("pringles.jpg")
def find_xy(event, x, y, flags, param):
    global hsv
    if event == cv.EVENT_LBUTTONDOWN:
        colors = hsv[x,y]
def main() :

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('image', find_xy)
    image= cv2.resize(img,(60,60))
    while(1):
        cv2.imshow('image',image)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
main()

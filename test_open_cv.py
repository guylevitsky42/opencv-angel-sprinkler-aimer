import numpy as np
import cv2


# Camera settings (default camera = 0)
# in order to include an incoming video stream, you should include IP:port address in the signature
# as explained in https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html
cap = cv2.VideoCapture(0)

while True:
    # captures a single frame
    ret, frame = cap.read()

    # Displays the frame on screen - waitKey is for macos.
    cv2.imshow('frame', frame)
    cv2.waitKey(1)


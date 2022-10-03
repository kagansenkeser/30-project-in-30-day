import cv2
import numpy as np
cap=cv2.VideoCapture(0)
background=cv2.imread("bggg.png")
background = cv2.resize(background, (800, 800))
while True:
    sas,img =cap.read()
    img=cv2.resize(img,(800,800))
    #aynı boyuta esitliyoruz
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([15, 97, 174])
    upper = np.array([27, 168, 255])

    mask = cv2.inRange(imgHSV, lower, upper)

    img[np.where(mask == 255)]=background[np.where(mask == 255)]
    cv2.imshow("img", img)
    cv2.imshow("mask", mask)
    cv2.waitKey(1)


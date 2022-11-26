import cv2
import numpy as np
from pynput.keyboard import Controller
from pynput.keyboard import Key, Controller

keyboard = Controller()
def empty(a):
    pass
img =np.zeros((512,512,3),np.uint8)
myColors=[[138,174,75,212,127,190]]
myColorvalues =[[0,0,255]]
myPoints = [] #[x,y,colorID]


#fonksiyonlar kısmı
def findColor(img,myColors,myColorvalues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newpoints=[]
    #normal rgb yi hsv ye çevirdik
    lower = np.array([138,75,127])
    upper = np.array([174,212,190])
    mask = cv2.inRange(imgHSV,lower,upper)
    x,y =getcontours(mask)
    cv2.circle(imgResult,(x,y),10,(0,0,255),cv2.FILLED)
    if x!= 0 and y!=0:
        newpoints.append([x,y,count])
    count +=1

    maskflip = cv2.flip(mask, 1)

    cv2.imshow("img",maskflip)
    return newpoints #sola kaydır

def getcontours(img):
    contours,hierarchy =cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h =0,0,0,0
    for cnt in contours:
        area =cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult,cnt,-1,(0,255,0),3)
            peri =cv2.arcLength(cnt,True)
            approx =cv2.approxPolyDP(cnt,0.02*peri,True)

            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y




cap =cv2.VideoCapture(0)
while True:
    #cv2.line()
    success, img = cap.read()
    imgResult = img.copy()
    cv2.line(imgResult, (320, 512), (320, 0), (0, 243, 3), 8)# y ekseni
    cv2.line(imgResult, (0, 320), (800, 320), (0, 243, 3), 8)# x ekseni
    newpoints = findColor(img, myColors, myColorvalues)


    for newp in newpoints:
        myPoints.append(newp)
        x=myPoints[-1][0]
        y=myPoints[-1][1]
        if y<330 and x>320:
            keyboard.press(Key.right)

        if y>330 and x>320:
            keyboard.release(Key.right)

        if y<330 and x<320:
            keyboard.press(Key.left)

        if y > 330 and x < 320:
            keyboard.release(Key.left)



    if len(myPoints) != 0:
        img_flip_lr = cv2.flip(imgResult, 1)
        cv2.imshow("RRRresult", img_flip_lr)
    # burası noklaraı silsin diye
    if cv2.waitKey(1) & 0xFF == ord("w"):
        myPoints = []
#                                    asdasd
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


import cv2
xlist=[4]
ylist=[4]
cap=cv2.VideoCapture(0)
x=0
y=0
n=0
a=0
xlist[0]=-3
ylist[0]=-3
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:

        print(x, ' ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        xlist[0]=x
        ylist[0] =y
        cv2.circle(img,(x,y),30,(0,255,255),10)
        a=x
        b=y
        global n
        cv2.imshow('image2', img)
        n=n+1
while True:
    succes, img=cap.read()
        # reading the image
    print(a)
        # displaying the image
    if xlist[0]>1:
        cv2.circle(img, (xlist[0], ylist[0] ), 30, (0, 0, 255), 10)

    cv2.imshow('image',img)

        # setting mouse handler for the image
        # and calling the click_event() function

    cv2.setMouseCallback('image', click_event)

    cv2.waitKey(1)

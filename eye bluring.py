import cv2
eyesCascade =cv2.CascadeClassifier("haarcascade_eye.xml")
cap =cv2.VideoCapture(1)
while True:
    
    success, img = cap.read()
    eyes = eyesCascade.detectMultiScale(img,1.1,8)
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 256),4)
        #gözlerin etrafına dikdörtgen çizmek için
        #draw a rectangle around  eyes

        img[y:y + h, x:x + w] = cv2.medianBlur(img[y:y + h, x:x + w], 21)
        #resmin sadece [y:y + h, x:x + w] olan kısmını blurlu olan ile değiştiriyoruz
        #we are puting part with blured instead of normal part
    cv2.imshow("vide2o", img)
    if cv2.waitKey(1)& 0xFF ==ord("q"):
        break

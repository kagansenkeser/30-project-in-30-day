import cv2
eyesCascade =cv2.CascadeClassifier("haarcascade_eye.xml")
cap =cv2.VideoCapture(1)
#kamera dan video almak için 0 çünkü dahili kamera
#taking value from camera 0 for main camera

while True:
    #döngü için
    #for loop
    succes, img = cap.read()
    #succes koyma sebebimiz
    #why is there succes
    #What cap.read() returns is a boolean (True/False) and image content. If you remove success, the img variable takes that boolean and image data as a tuple. This is why you get an error.
    eyes = eyesCascade.detectMultiScale(img,1.1,8)
    #resimdeki gözleri bulmak için
    #for detect eyes in img
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #gözlerin etrafını kareye almak için
    #draw a rectangle around eyes

    cv2.imshow("video",img)
    if cv2.waitKey(1)& 0xFF ==ord("q"):
        break
    

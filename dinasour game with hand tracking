import cv2
import mediapipe as mp
import time
from pynput.keyboard import Controller
from pynput.keyboard import Key, Controller

#kütüphne bunlar geç





cap =cv2.VideoCapture(0)
#video yu alma
mpHands =mp.solutions.hands
#formalite bu kodları kullanmak için
#elleri tanımlama
keyboard = Controller()
hands = mpHands.Hands()
#mphands fonksiyon mp den gele

mpDraw =mp.solutions.drawing_utils
#çizmek için bunu ekledik başta fonksiyon gibi üdşün

pTime = 0
#previous time
cTime = 0
#current time

nokta2y = int
nokta1x = int
nokta2x = int
nokta1y = int
while True:
    #döngü aktif işte
    success,img=cap.read()
    #succes bi şart olsun diye  ve resmi cameranın çektiği görüntüye eşitliyoruz
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #Rgb ye çivridk çünkü hands fonksiyonu sadece rgb seviyo
    results = hands.process(imgRGB)
    #hands işlemini img rgb ye uyulguyor bunu da results a atyoruz


    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
    #birden fazla nokta olduğu için çokça el pointi dedik
        for handLms in results.multi_hand_landmarks:
            # her el pointi için
            for id,lm in enumerate(handLms.landmark):
                # noklatarin id sini almak için

                #print(id,lm)
                # bu her noktantin kordinatii verio ama sorun şu ki  istemiz pixel şeklinde vemrio
                h,w,c=img.shape
                cx,cy,=int(lm.x*w),int(lm.y*h)
                # şu anki istemiz formaya çevirdik int olsun ki tam sayı olsun
                #print (id,cx,cy)
                if id == 4 :
                    cv2.circle(img,(cx,cy),20,(0,0,0),cv2.FILLED)
                    nokta1x =cx
                    nokta1y =cy
                    #print(id, cx, cy)
                elif id == 8 :
                    cv2.circle(img,(cx,cy),20,(0,0,0),cv2.FILLED)
                    nokta2x = cx
                    nokta2y = cy
                    #print(id, cx, cy)

            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
            #direk çizmek için bi nevi fonkisyon gibi çağrdık başta ekltip
            #HAND CONNECTİON otamatik library de var
    #print("nokta bir",nokta1x,nokta1y,"nokta 2 ",nokta1x,nokta2y)

#
    #print (uzaklik)
    cTime = time.time()
    #su anki zamanı vercek
    fps= 1/(cTime-pTime)
    pTime = cTime
    #buralar fps için
    #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    uzaklik = ((nokta1x - nokta2x) * (nokta1x - nokta2x)) + ((nokta1y - nokta2y) * (nokta1y - nokta2y))
    print (uzaklik)
    #
    if  uzaklik<5000:
        keyboard.press(Key.space)
        keyboard.release(Key.space)

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,4,(255,0,255),5)
    #bu ekrana yazı yazdrma için güzel şey öğren bunu yaz kenara lazım olur


    cv2.imshow("image",img)
    #can dostumuz gösterici


    cv2.waitKey(1)
    #can dostumuzun kardeşi 1 salise ekranda tut öbür türlü takılı kalır 0 da

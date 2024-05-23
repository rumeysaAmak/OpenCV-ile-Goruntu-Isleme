# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:15:54 2024

@author: Lenovo
"""
# Bu kütüphaneler, görüntü işleme ve el tespiti gibi işlemleri gerçekleştirmemize olanak tanır.
import cv2
import mediapipe as mp

#cv2.VideoCapture(0) kullanarak bir video yakalama nesnesi oluşturuyoruz. Bu, bilgisayarınıza bağlı bir kameradan görüntü almak için kullanılır. Ardından, görüntünün genişliğini ve yüksekliğini belirliyoruz.
cap =cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

#mediapipe kütüphanesini kullanarak el tespiti yapmak için gerekli nesneleri oluşturuyoruz.
mpHand=mp.solutions.hands
hands= mpHand.Hands()
mpDraw =mp.solutions.drawing_utils

#Eldeki parmakların uçlarını takip etmek için kullanacağımız indeksleri belirliyoruz
tipIds=[4,8,12,16,20]

#Sonsuz bir döngü oluşturuyoruz. Bu döngü, her bir kareyi almak, el tespitini yapmak, eldeki parmakları saymak ve ekrana çizmek için kullanılacak.
while True:
    
    success, img =cap.read()#Kameradan bir kare alıyoruz ve başarılı bir şekilde alınıp alınmadığını kontrol ediyoruz.
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#Alınan kareyi RGB formatına dönüştürüyoruz, çünkü mediapipe kütüphanesi bu formatta işlem yapar.
    
    results= hands.process(imgRGB)#El tespiti yapılıyor ve sonuçlar results değişkenine atanıyor. Bu sonuçlarda, elin parmak uçlarının koordinatları bulunur.
    print(results.multi_hand_landmarks)
    
    lmList=[]
    #Eğer el tespiti sonuçlarında birden fazla el bulunmuşsa, her bir el için aşağıdaki işlemleri yapacağız.
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handLms,mpHand.HAND_CONNECTIONS)#Eldeki parmak uçlarını ve elin çizgilerini çiziyoruz.
            
            #Her bir parmağın uç koordinatlarını lmList listesine ekliyoruz.
            for id, lm in enumerate(handLms.landmark):
                h,w,_=img.shape
                cx, cy=int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])
                
                #işaret uç  = 8 
                #if id == 8:
                    #cv2.circle(img,(cx,cy),9,(255,0,0),cv2.FILLED)
                
                #işaret uç  = 6 
                #if id == 6:
                    #cv2.circle(img,(cx,cy),9,(0,0,255),cv2.FILLED)
             
            #Bu kod bloğu, eldeki her bir parmağın açık veya kapalı olup olmadığını belirler ve bu bilgileri fingers listesine kaydeder.       
            if len(lmList)!=0: #lmList listesinde en az bir el tespit edildiğini kontrol eder. Eğer lmList boş değilse, yani en az bir el tespit edilmişse, bu bloğa girilir.
                fingers=[] #fingers adında boş bir liste oluşturulur. Bu liste, her bir parmak için bir "açık" veya "kapalı" durumunu tutacaktır.
                
                #baş parmak için:if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:: Baş parmağın ucu (tip) ile baş parmağın bir önceki ekleminin ucu arasındaki x koordinatlarını karşılaştırır. Eğer baş parmağın ucu, bir önceki eklemin ucundan daha sol tarafta (daha küçük x koordinatına sahip) ise, bu durumda baş parmak açıktır ve fingers listesine 1 eklenir. Aksi takdirde, baş parmak kapalıdır ve fingers listesine 0 eklenir. 
                if lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                
                #diğer 4 parmak:Her parmak için, parmağın ucu (tip) ile aynı parmağın bir önceki ekleminin ucu arasındaki y koordinatlarını karşılaştırır. Eğer parmağın ucu, bir önceki eklemin ucundan daha yukarıda (daha küçük y koordinatına sahip) ise, bu durumda parmak açıktır ve fingers listesine 1 eklenir. Aksi takdirde, parmak kapalıdır ve fingers listesine 0 eklenir.   
                for id in range(1,5):
                    if lmList[tipIds[id]][2]< lmList[tipIds[id]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
               
                #fingers.count(1): fingers listesindeki elemanların sayısını sayar ve değeri 1 olanların sayısını bulur. Burada, 1 olanlar, parmağın açık olduğunu veya dik konumda olduğunu temsil eder. count(1) metodu bu durumu sayar.
                #totalF = fingers.count(1): Yukarıdaki adımda sayılan açık parmakların toplam sayısını totalF değişkenine atar.
                #cv2.putText(img, str(totalF), (30, 125), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 8): putText() fonksiyonu, bir görüntüye metin yazdırmak için kullanılır. Bu satırda, metin görüntüye yazdırılır.
                #str(totalF): Görüntüye yazılacak metin, yani açık parmakların toplam sayısı. totalF değişkeni str() fonksiyonuyla stringe dönüştürülür, çünkü putText() fonksiyonu sadece string türündeki metinleri alır.
                #(30, 125): Metnin başlangıç konumu. Burada (x, y) koordinatları belirtilir. Metin, sol üst köşesinden başlayarak bu konuma göre yerleştirilir.
                #cv2.FONT_HERSHEY_PLAIN: Kullanılacak yazı tipi.
                #10: Yazı büyüklüğü.
                #(255, 0, 0): Metnin rengi. Burada mavi renk kullanılır. Renkler için (BGR) formatı kullanılır.
                #8: Metnin kalınlığı. Bu değer ne kadar büyük olursa, metin o kadar kalın olur.
                totalF= fingers.count(1)
                cv2.putText(img,str(totalF),(30,125),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),8)
                
                
    #Son olarak, işlenmiş kareyi ekranda gösteriyoruz ve bir tuşa basılmasını bekliyoruz.                
    cv2.imshow("img",img)
    cv2.waitKey(1)
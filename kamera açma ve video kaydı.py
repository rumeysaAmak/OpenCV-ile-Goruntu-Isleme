# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 17:41:41 2024

@author: Lenovo
"""
#kamera açma ve video kaydı
import cv2

#capture 

cap= cv2.VideoCapture(0)

width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#640
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))#480

print(width,height)

#video kaydet

writer = cv2.VideoWriter("video_kaydı.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,(640,480))
#cv2.VideoWriter_fourcc(*"DIVX"): Video sıkıştırma formatını belirtir. Bu durumda, DIVX sıkıştırma formatı kullanılacaktır. DIVX, AVI formatında sıkıştırma için oldukça yaygın bir formatı temsil eder.
#20: Video'nun FPS (Frame Per Second - Saniyedeki Kare Sayısı) değerini belirtir. Bu durumda, video 20 FPS ile oluşturulacak. Yani her saniyede 20 kare gösterilecek.
#Bu kod, belirtilen parametrelerle birlikte bir VideoWriter nesnesi oluşturur. Bu nesne, videonun kaydedilmesi için kullanılacak olan bir araçtır.

while True:
    ret ,frame =cap.read()
    cv2.imshow("video",frame)
    
    #save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF ==ord("q"): # q ya bastığında idtediğin yerde videoyu kapatabilirsin
        break
cap.release()# stop capture(video bittiğinde durdur)
writer.release() #yazmayı durdur  
cv2.destroyAllWindows()#bütün açık olan pencereleri kapat   
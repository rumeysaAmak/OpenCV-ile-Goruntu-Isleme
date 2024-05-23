# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:57:13 2024

@author: Lenovo
"""

#video içe aktarma

import cv2
import time 

video_name=r'C:\Users\Lenovo\.spyder-py3\rumeysa.mp4'

# video içe aktar = capture,cap

cap=cv2.VideoCapture(video_name)

print("video genişliği:",cap.get(3))
print("video yüksekliği:",cap.get(4))


# videonun cap a yüklenip yüklenmediğini kontrol etmeliyiz
if cap.isOpened()== False:
    print("hata")
    
#video okunması (bundan önce sadece resim olarak aktarır bunu döngülerle video yapmalısın)

while True:
    ret, frame=cap.read() #ret=return
    if ret ==True:
        time.sleep(0.1)#eğer bunu kullanmazsak çok hızlı akar
        
        cv2.imshow("video",frame)
    else: break
     
    if cv2.waitKey(1) & 0xFF ==ord("q"): # q ya bastığında idtediğin yerde videoyu kapatabilirsin
        break
        
cap.release()# stop capture(video bittiğinde durdur)
    
cv2.destroyAllWindows()#bütün açık olan pencereleri kapat
    
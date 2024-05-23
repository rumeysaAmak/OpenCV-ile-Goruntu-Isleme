# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:35:35 2024

@author: Lenovo
"""

import cv2
import numpy as np

#numpy ile resim oluştur
image=np.zeros((512,512,3),np.uint8)#512 ye 512lik 3 boyutlu siyah beyaz bir resim
#zeros=siyah bir görüntü oluşması için kullanılır. 1 yapsaydık beyaz bir görüntü oluşacaktı

print(image.shape)#512ye 512 3 boyutlu

cv2.imshow("siyah resim",image)

#resmin üzerine çizgi ekleyelim

cv2.line(image,(100,100),(100,300),(0,255,0),3)#(resim,başlangıç noktası,bitiş noktası,renk,kalınlık) formatında olur.
#(0,255,0)=yeşil renk
cv2.imshow("cizgi",image)

#dikdörtgen
#(resim,başlangıç noktası,bitiş noktası,renk)
cv2.rectangle(image,(0,0),(256,256),(255,0,0),cv2.FILLED)#CV2.FILLED=dikdörtgenin içini doldurmak için 
cv2.imshow("dikdortgen",image)

#çember , daire
#resim,merkez,yarı çap,renk
cv2.circle(image, (300,300),45,(0,0,255))#daire içinse çemberin içini doldurmamız yeterli. cv2.fılled ile yapabilirsin
cv2.imshow("cember",image)

#metin ekleyelim
#(resim,başlangıç noktası,yazı tipi,kalınlığı,renk)
cv2.putText(image,"rumeysa",(350,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.imshow("metin",image)
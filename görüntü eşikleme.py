# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 15:11:28 2024

@author: Lenovo
"""

import cv2
import matplotlib.pyplot as plt

img =cv2.imread(r'C:\Users\Lenovo\.spyder-py3\agac.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#grayscale'e çevirdik

plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")

#eşikleme fonksiyonu 
#amaç filtreleyerek nesneleri ön plana çıkarma
_, thresh_img=cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh_img,cmap="gray")
plt.axis("off")


_, thresh_img=cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY_INV)

plt.figure()
plt.imshow(thresh_img,cmap="gray")
plt.axis("off")

#uyarlamalı eşik değeri = bu işlem yapılırken küçük detayların resimde kaybolmaması.Bütünlüğün kaybolmaması.
thresh_img2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)#FONKSİYONDUR
plt.figure()
plt.imshow(thresh_img2,cmap="gray")
plt.axis("off")



















# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:07:36 2024

@author: Lenovo
"""

#yeniden boyutlandır ve kırp

import cv2

img = cv2.imread(r'C:\Users\Lenovo\.spyder-py3\rumeysa.jpeg')
print("resim boyutu: ",img.shape)

cv2.imshow("orijinal",img)

#♥yeniden boyutlandır
img2=cv2.resize(img,(1000,1000))#resize=yeniden boyutlandır

print("resized",img2.shape)

cv2.imshow("img2", img2)

#kırpma işlemi

imgCropped = img[0:800,0:900]

cv2.imshow("kırpılmıs resim",imgCropped) 

#görüntüyü netleştirmek için yeniden okut(okutmazsan fark etmez img ile devam edebilirsin)
image = cv2.imread(r'C:\Users\Lenovo\.spyder-py3\rumeysa.jpeg')

blurred_image = cv2.GaussianBlur(image, (5, 5), 0)#bulunduğu pikselin parlaklığını, çevresindeki pikselleri çan eğrisi fonksiyonuyla halvet eyleyip ağırlıklı ortalama alarak düzelten yumuşatma şeklidir.

# Netleştirilmiş görüntüyü göster
cv2.imshow('Netleştirilmiş Görüntü', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:18:15 2024

@author: Lenovo
"""

import cv2

import numpy as np

img=cv2.imread(r'C:\Users\Lenovo\.spyder-py3\kalp10.jpg')

cv2.imshow("kart",img)

print(img.shape)
width=300
height=300

#resimin köşe noktalarını pointler şeklinde oluşturalım
pts1= np.float32([[131,0],[0,239],[300,86],[173,328]])#çevirmek istediğim resmimin köşeleri

pts2= np.float32([[0,0],[0,height],[width,0],[width,height]])#düz olması için ekranın köşeleri

matrix = cv2.getPerspectiveTransform(pts1,pts2)

print(matrix)

imgOutput=cv2.warpPerspective(img, matrix,(width,height))
cv2.imshow("duzlestirilmis resim",imgOutput)
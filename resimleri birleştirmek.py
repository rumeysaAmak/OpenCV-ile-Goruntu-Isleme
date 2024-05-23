# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:07:11 2024

@author: Lenovo
"""
import cv2
import numpy as np
#resmi içe aktar

img= cv2.imread(r'C:\Users\Lenovo\.spyder-py3\rumeysa.jpeg')
cv2.imshow("resim", img)


#horizontal = yanyana birleştirme.(yatay)

hor=np.hstack((img,img))
cv2.imshow("horizontal",hor)

#vertical= dikey birleştirmek
ver= np.vstack((img,img))
cv2.imshow("vertical",ver)

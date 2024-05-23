# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:34:22 2024

@author: Lenovo
"""

import cv2

# resim içe aktarma

img= cv2.imread(r'C:\Users\Lenovo\.spyder-py3\rumeysa.jpeg',0) # 0 koyarsak resmi grayscale olarak içe aktarır

#görselleştir

cv2.imshow("ilk resim",img)

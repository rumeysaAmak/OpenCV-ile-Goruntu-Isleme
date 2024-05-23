# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:27:32 2024

@author: Lenovo
"""

#gradyanlar: görüntü gradyanı. görüntüdeki yoğunluk veya renkteki yönlü değişikliktir..kenar algılamada kullanılır
import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread(r'C:\Users\Lenovo\.spyder-py3\Sudoku.jpg',0)
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.title("orijinal")

#x gradyanlatı: görüntüdeki x eksenlerinin tespiti
sobelx=cv2.Sobel(img, ddepth=cv2.CV_16S, dx=1, dy=0,ksize=5)
plt.figure()
plt.imshow(sobelx,cmap="gray")
plt.axis("off")
plt.title("sobelx")

#y gradyanı: görüntüdeki y eksenlerinin tespiti
sobely=cv2.Sobel(img, ddepth=cv2.CV_16S, dx=0, dy=1,ksize=5)
plt.figure()
plt.imshow(sobely,cmap="gray")
plt.axis("off")
plt.title("sobely")

#laplacioan gradyan: her iki eksenin de tespiti
laplacioan= cv2.Laplacian(img, ddepth=cv2.CV_16S)
plt.figure()
plt.imshow(laplacioan,cmap="gray")
plt.axis("off")
plt.title("laplacioan")



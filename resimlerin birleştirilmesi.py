# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 17:38:33 2024

@author: Lenovo
"""

import cv2
import matplotlib.pyplot as plt

img1=cv2.imread(r'C:\Users\Lenovo\.spyder-py3\kalp10.jpg')
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)#rengi convert etmemiz lazım.yoksa mavi görüntü ortaya çıkar

img2=cv2.imread(r'C:\Users\Lenovo\.spyder-py3\rumeysa.jpeg')
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)



#aynı boyutta olmaları lazım öyle birleştirebiliriz.
print(img1.shape)#(331, 302, 3)
print(img2.shape)#(825, 825, 3)
#boyutları farklıymış.Boyutları eşitleyelim
img1=cv2.resize(img1,(300,300))
img2=cv2.resize(img2,(300,300))
print(img1.shape)#(300, 300, 3)
print(img2.shape)#(300, 300, 3)

plt.figure()
plt.imshow(img1)
plt.show()

plt.figure()
plt.imshow(img2)
plt.show()

#karıştırılmış resim =alpha*img1+beta*img2
blended= cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)#blended hazır fonksiyondur.0.5 yazmamızın sebebi ise iki resimi birleştirmek istememiz.
#alphaya 1 betaya 0 yazsaydım sadece img1 görünürdü.yani hangi resimden ne kadar miktarda alacağımızı gösterir bu değerler.
plt.figure()
plt.imshow(blended)










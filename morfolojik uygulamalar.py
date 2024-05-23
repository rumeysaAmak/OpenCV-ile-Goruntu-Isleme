# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:10:50 2024

@author: Lenovo
"""

#erozyon: ön plandaki nesnenin sınırlarını aşındırır
#genişleme: görüntüdeki beyaz bölgeyi arttırır
#açma: açılma, erozyon+genişlemedir.gürültünün giderilmesinde faydalıdır
#kapatma: amanın tam tersidir. genişleme+erozyon.ön plandaki nesnelerin içindeki küçük delikleri veya nesne üzerindeki küçük siyah noktaları kapatmak için kullanışlıdır.
#morfolojik gradyan: bir görüntünün genişlemesi ve erozyonu arasındaki farktır.
 
import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread(r'C:\Users\Lenovo\.spyder-py3\Instagram-Siyah-Ekran.jpg',0)

plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.title("orijinal")

#erozyon:sınırları küçültme=erode
kernel=np.ones((5,5),dtype=np.uint8)
result=cv2.erode(img, kernel,iterations=1)#iterasyonu arttırdıkça sınırlar küçülür.
plt.figure()
plt.imshow(result,cmap="gray")
plt.axis("off")
plt.title("erozyon")

#genişlme=dilation
result2=cv2.dilate(img, kernel,iterations=1)
plt.figure()
plt.imshow(result2,cmap="gray")
plt.axis("off")
plt.title("genişleme")

#açılma:beyaz gürültüyü yok eder. o yüzden önce bir beyaz gürültü oluşturalım
#whiteNoise
whiteNoise = np.random.randint(0,2, size=img.shape[:2])
whiteNoise= whiteNoise*255

plt.figure()
plt.imshow(whiteNoise,cmap="gray")
plt.axis("off")
plt.title("beyaz gürültü")

#bu gürültüyü orijinal resme eklemeliyiz

noise_image=whiteNoise+img
plt.figure()
plt.imshow(noise_image,cmap="gray")
plt.axis("off")
plt.title("gürültülü resim")

#şimdi ise açılma yöntemiyle bu gürültülü resimi açıcaz

opening=cv2.morphologyEx(noise_image.astype(np.float32),cv2.MORPH_OPEN,kernel)
plt.figure()
plt.imshow(opening,cmap="gray")
plt.axis("off")
plt.title("açılmış resim")

#kapatma:kapatma işlemini uygulayabilmek için önce black noise eklememiz lazım
#black noise
blackNoise = np.random.randint(0,2, size=img.shape[:2])
blackNoise= blackNoise*-255

plt.figure()
plt.imshow(blackNoise,cmap="gray")
plt.axis("off")
plt.title("siyah gürültü")


#bu gürültüyü orijinal resme eklemeliyiz

noise_image2=blackNoise+img
plt.figure()
plt.imshow(noise_image2,cmap="gray")
plt.axis("off")
plt.title("siyah gürültülü resim")

closing=cv2.morphologyEx(noise_image2.astype(np.float32),cv2.MORPH_CLOSE,kernel)
plt.figure()
plt.imshow(closing,cmap="gray")
plt.axis("off")
plt.title("kapama")

#gradient: kenar tespiti
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
plt.figure()
plt.imshow(gradient,cmap="gray")
plt.axis("off")
plt.title("gradyan")












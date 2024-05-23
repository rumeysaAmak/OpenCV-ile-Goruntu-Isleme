# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 17:00:30 2024

@author: Lenovo
"""

#görüntü bulanıklığı , görüntünün düşük geçişli bir filtre uygulanmasıyla elde edilir.
#görüntüyü gidermek için kullanışlıdır.
#görüntüden yüksek frekanslı içeriği kaldırı
#opencv 3 ana tür bulanıklaştırma sağlar:ortalama,gauss,medyan

import cv2
import matplotlib.pyplot as plt
import warnings 
import numpy as np
warnings.filterwarnings("ignore")#koddaki uyarıları kaldırmak için kullanılır

#blurring (detayı azaltır,gürültüyü engeller)

img=cv2.imread(r'C:\Users\Lenovo\.spyder-py3\NYC.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("original")

#ortalama bulanklaştırma yöntemi
dts2=cv2.blur(img,ksize=(3,3))
plt.figure()
plt.imshow(dts2)
plt.axis("off")
plt.title("ortalama blur")


#gaussian blur
gb= cv2.GaussianBlur(img, ksize=(3,3,), sigmaX=7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("gauss blur")


#medyan blur
mb=cv2.medianBlur(img, ksize=(3,3))
plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.title("medyan blur")


#GAUSS GÜRÜLTÜSÜ OLUŞTURMA
def gauusianNoise(image): #fonksiyon tanımı ile başlarız
    row,col,ch=image.shape  # İlk olarak, gürültü eklenmeden önceki görüntünün boyutlarını alırız.row ve col, görüntünün yüksekliği ve genişliği olarak alınırken, ch ise görüntünün kanal sayısını (RGB görüntülerde 3) belirtir.
    mean=0        #Gauss gürültüsü eklemek için gerekli olan parametreler tanımlanır. 
    var=0.05      #mean, eklenen gürültünün ortalama değeridir. var, gürültünün varyansını belirler ve sigma standart sapmayı hesaplamak için kullanılır. 
    sigma=var**0.5 
    
    #Belirtilen ortalama ve standart sapma ile normal dağılıma sahip Gauss gürültüsü oluşturulur.
    gauss=np.random.normal(mean,sigma,(row,col,ch))#np.random.normal() fonksiyonu, belirtilen ortalama ve standart sapmaya sahip bir normal dağılım üzerinden rastgele değerler üretir. Bu, gauss dizisine görüntü boyutlarına uygun bir şekilde üretilen gürültü eklenir.
    gauss=gauss.reshape(row,col,ch)#Bu, gauss dizisini, row, col ve ch boyutlarına sahip bir diziye dönüştürür.
    noisy=image+gauss#Oluşturulan Gauss gürültüsü, orijinal görüntüye eklenir.Bu adımda, her piksel değeri, gürültü ile birlikte ilgili pikselin orijinal değeri ile toplanır.
    
    return noisy#Bu, gürültü eklenmiş görüntüyü çağıran kod parçasına geri döndürür.


#gürültüyü ekleyebilmek için görüntüyü normalize etmeliyiz.    
img=cv2.imread(r'C:\Users\Lenovo\.spyder-py3\NYC.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255 #normalize edildi 0-255 arasında olan resmi 0-1 arasına yerleştirdik.
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("original")    
 
gaussianNoiseImage= gauusianNoise(img)
plt.figure()
plt.imshow(gaussianNoiseImage)
plt.axis("off")
plt.title("gauss noisy")                                 
    

#şimdi ise oluşturduğumuz gürültüyü gauss blur ile azaltacağız
gb=cv2.GaussianBlur(img, ksize=(3,3), sigmaX=7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("gauss blur2")

#TUZ KARABİBER GÜRÜLTÜSÜ OLUŞTURMAK(RESMİN ÜZERİNE SİYAH BEYAZ NOKTALARIN RASTGELE DAĞILMASI)
def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5  # Tuz ve biber oranı
    amount = 0.004 # Gürültü miktarı
    noisy = np.copy(image) #Orijinal görüntünün bir kopyası oluşturulur. Bu, üzerine tuz-biber gürültüsü eklenecek görüntüyü temsil eder.
    
    # Salt (beyaz) gürültü:num_salt, tuz parçacıklarının sayısını belirler. Daha sonra, bu tuz parçacıklarının konumları, rastgele belirlenir ve noisy üzerine beyaz olarak yerleştirilir.
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, high=i, size=int(num_salt)) for i in image.shape]
    noisy[coords[0], coords[1], :] = 1  # Tüm kanallar için beyaz
    
    # Pepper (siyah) gürültü:num_pepper, biber parçacıklarının sayısını belirler. Daha sonra, bu biber parçacıklarının konumları, rastgele belirlenir ve noisy üzerine siyah olarak yerleştirilir.
    num_pepper = np.ceil(amount * image.size * (1.0 - s_vs_p))
    coords = [np.random.randint(0, high=i, size=int(num_pepper)) for i in image.shape]
    noisy[coords[0], coords[1], :] = 0  # Tüm kanallar için siyah
    
    return noisy #

spImage=saltPepperNoise(img)    
plt.figure()
plt.imshow(spImage)
plt.axis("off")
plt.title("saltPepperNoise")     
    
#şimdi ise bu gürültüyü yok etmek için medyan blur uygulayacağız
mb2=cv2.medianBlur(spImage.astype(np.float32), ksize=(3))# Median blur uygulanacak görüntüyü belirtelim ve float32'ye dönüştürelim.
plt.figure()                                             ## ksize argümanı (3,3) yerine 3 olarak belirtiliyor
plt.imshow(mb2)
plt.axis("off")
plt.title("medyan blur2")    
    
    
    
    
    
    
    

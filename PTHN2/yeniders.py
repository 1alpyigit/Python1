
#Dosya acma okuma yazma ekleme

#with open('metin.txt', 'c') as create:
#    icerik = create.
#with open('metin.txt', 'r') as acma:
#    icerık = acma.read()
#    print(icerık)


#with open('yeni_metin.txt', 'w') as yazma:
#    yazma.write("Bu dosyaya yazılan metin. \nYeni yazı")

#with open('metin.txt', 'a') as ekleme:
#    ekleme.write("\nYeni bir satır ekledik.")        


#with open('resim.jpg', 'rb') as foto:
#    icerik = foto.read()
#    print(icerik)

#with open('ses.wav', 'wb') as voild:
#    veri = b'\x52\x49...'    
#    dosya.write(veri)

#dosyadankeliimebulma

#def kelimebul(dosyaadı, aranankelime):
#    with open(dosyaadı, 'r') as dosya:
#        satırnumarası = 0
#        bulunankonum = []
#
#        for satır in dosya:
#            satırnumarası += 1 
#            konum =-1
#            while True:
#                konum = satır.find(aranankelime, konum + 1)
#                if konum == -1:
#                    break
#                bulunankonum.append((satırnumarası, konum))
#    return bulunankonum

#dosyaadı = 'ornek_metin.txt'
#aranankelime = 'Python'

#bulunanlar = kelimebul(dosyaadı, aranankelime)
#for satırnumarası, konum in bulunanlar:
#    print(f"'{aranankelime}' kelimesi, Satır: {satırnumarası}, İndis: {konum}")

#dosyaadı = 'ornek_metin.txt'
#with open('ornek_metin.txt', 'w') as dosya:
#    dosya.write("Bı bir Python dosyasıdır.\nBu kadar!")

#file = open('ornek_metin.txt', 'w')
#file.close()

#file = open('ornek_metin.txt', 'w')
#file.write("Bu bir Python dosyasıdır.\n Yeni bir satır")

#file = open("C:/users/user/desktop/ornek_metin.txt", "w")
#file.close()

#KARIŞTIRMADOSYASI


#import random
#dosyaadı= 'ornek_metin.txt'
#with open(dosyaadı, 'r') as dosya:
#    satırlar = dosya.readlines()
#random.shuffle(satırlar)
#with open("C:/users/user/desktop/cıktı.txt", "w") as dosya:
#    for satır in satırlar:
#        dosya.write(satır)

#dosyaadı = "C:/users/user/desktop/ornek_metin.txt"
#with open("C:/users/user/desktop/ornek_metin.txt", "r") as dosya:
#    ıcerik= dosya.read()
#karaktersayısı = len(ıcerik)
#print(f"'{dosyaadı}' dosyasındaki toplam karakter sayısı: {karaktersayısı} ") 

#Dosya içi bakmalar

#dosyaadi = "C:/users/user/desktop/ornek_metin.txt"

#with open(dosyaadi, 'r') as dosya:
#    icerik = dosya.read()

#toplamkaraktersayisi = len(icerik)

#bosluksayisi = icerik.count(' ')
#satirsonusayisi = icerik.count('\n')
#ozelkaraktersayisi = toplamkaraktersayisi - (icerik.count('\n') + icerik.count(' ') + icerik.count('\t') + icerik.count('\r'))

#print(f"'{dosyaadi}' dosyasındaki toplam karakter sayısı: {toplamkaraktersayisi}")
#print(f"Boşluk sayısı: {bosluksayisi}")
#print(f"Satır sonu karakteri sayısı: {satirsonusayisi}")
#print(f"Özel karakterlerin sayısı: {ozelkaraktersayisi}")


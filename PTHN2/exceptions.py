#Temel hata kontrolü
#dosya kontroleri

#dosyaadı= 'ornek_metin.txt'
#aranankeime = 'Python'
#try:
#    with open(dosyaadı, 'r') as dosya:
#        icerik = dosya.read()
#        kelimesayısı= icerik.count(aranankelime)
#        print(f"'{dosyaadı}' dosyasında '{aranankelime}' kelimesi {kelimesayısı} kez geçiyor)
#except FileNotFoundError:
#    print(f"'{dosyaadı}' dosya bulunamadı!")      



#dosyaadi = 'ornek_metin.txt'
#try:
#    with open(dosyaadi, 'r') as dosya:
#        # Dosya içeriğini okuma
#        icerik = dosya.read()
#        print(icerik)
#except IOError:
#    print("Dosya okuma hatası!")


#dosyaadi = 'yeni_dosya.txt'
#try:
#    with open(dosyaadi, 'w') as dosya:
#        dosya.write("Bu dosyaya yazılan metin.\nYeni bir satır.")
#except IOError:
#    print("Dosya yazma hatası!")

#örnek

#dosyaadı= 'ornekdosya.txt'

#try:
#    with open(dosyaadı, 'r') as dosya:
#        icerik = dosya.read()
#        karaktersayılarıı = {}
#        for karakter in icerik:
#            if karakter in karaktersayılarıı:
 #               karaktersayılarıı[karakter] += 1
 #           else:
#                karaktersayılarıı[karakter] = 1
#        for karakter, say in karaktersayılarıı.items():
#            print(f"'{karakter}': {say}")
#except FileNotFoundError:
#    print(f"'{dosyaadı}' dosyası bulunamadı.")      

#dosyaadi = 'metin.txt'

#try:
#    with open(dosyaadi, 'r') as dosya:
#        icerik = dosya.read()
#    with open('buyukharfmetin.txt', 'w') as dosya:
#        dosya.write(icerik.upper())
#    with open('kucukharfmetin.txt', 'w') as dosya:
#        dosya.write(icerik.lower())
#except FileNotFoundError:
#    print(f"'{dosyaadi}' dosyası bulunamadı.")
#finally:
#    dosya.close()
 #   print("Dosya kapatıldı.")

#dosyaadi = 'ornek.txt'

#try:
#    dosya = open(dosyaadi, 'r')
#    icerik = dosya.read()
#    print(icerik)
#except FileNotFoundError:
#    print(f"'{dosyaadi}' dosyası bulunamadı.")
#finally:
#    try:
#        dosya.close()
#        print("Dosya kapatıldı.")
#    except UnboundLocalError:
#        print("Dosya zaten kapatılmış veya dosya bulunamadı.")

#Yazma izni olmayan dosya hatası

#dosyaadi = 'yazmaizinolmayan.txt'
#metin= "Bu dosya yazmak istiyoruz"
#try:
#    with open(dosyaadi, 'a') as dosya:
 #       dosya.write(metin + '\n')
 #       print(f"'{dosyaadi}' dosyasına yazma işlemi tamamlandı.")
#except PermissionError:
#    print(f"'{dosyaadi}' dosyasına yazma izni bulunmamaktadır.")
#except FileNotFoundError:
#    print(f"'{dosyaadi}' dosyası bulunamadı.")



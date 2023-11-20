                 #kitap.py
 
#import os
#class Kitap:
#    def __init__(self, baslık, yazar, sayfasayısı):
#        self.baslık = baslık
#        self.yazar = yazar
#        self.sayfasayısı = sayfasayısı
#        self.okundumu = False
#    def kitapbilgileri(self):
#        print(f"Kitap: {self.baslık}, Yazar: {self.yazar}, Sayfa Sayısı: {self.sayfasayısı}, Okundu mu: {'Evet' if self.okundumu else 'Hayır'} ")
#
                    #main.py
#from kitap import Kitap
#def main():
#    kitaplar = []

#    while True:
#        os.system('cls')
#        print("Yeni kitap ekle (Çıkmak için 'q' tuşuna basın)")
#        baslık = input("Kitap Adı: ")
#        if baslık.lower() == 'q':
#            break
#        yazar = input("Yazar Adı: ")
#        sayfasayısı = int(input("Sayfa Sayısı: "))
#
#        kitap = Kitap(baslık, yazar, sayfasayısı)
#        kitaplar.append(kitap)

#    print("\nOkunan kitapları işaretleme")
#    for index, kitap in enumerate(kitaplar, 1):
#        print(f"\n{index}. Kitap:")
#        kitap.kitapbilgileri()

#    okundumu = input("Bu kitabı okudunuz mu? (Evet için 'e' girin): ").lower()
#    if okundumu == 'e':
#        kitap.okundumu = True

#    print("\nOkunan ve okunmayan kitaplar: ")
#    for index, kitap in enumerate(kitaplar, 1):
#        if kitap.okundumu:
#            print(f"\n{index}. Okunan Kitap: ")
#            kitap.kitapbilgileri()
#        else:
#            print(f"\n{index}. Okunmayan kiyaplar:")
#            kitap.kitapbilgileri()    

#if __name__ == "__main__":
#    main()
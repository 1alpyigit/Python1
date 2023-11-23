#class calısan:
#    def __init__(self, ad, soyad, pozisyon):
#        self.ad = ad
#        self.soyad = soyad
#        self.pozisyon = pozisyon

 #   def __str__(self):
#        return f"{self.ad} {self.soyad}, {self.pozisyon}"
    
#class ısyeri:
#    def __init__(self):
#        self.calısanlar = []
#    def calısan_ekle(self, calısan):
#        self.calısanlar.append(calısan)
#    def calısan_listele(self):
#        if not self.calısanlar:
#            print("Henüz çalışan kaydı yoktur.")
#        else:
#            print("çalışanlar: ")
#            for idx, calısan in enumerate(self.calısanlar, start=1):
#                print(f"{idx}. {calısan}")

#    def calısansıl(self, index):
#        if 0< index <= len(self.calısanlar):
#            silinecekcalısan= self.calısanlar.pop(index-1)
#            print(f"{silinecekcalısan} silindi.")
#        else:
#            print("Gereksiz.")

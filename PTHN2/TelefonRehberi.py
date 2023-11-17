import os
rehber = {}


def ekle():
    ad = input("İsim:")
    tel= input("Numara:")
    rehber.update({ad : tel})
    print(ad, " eklendi...")
def ara():
    ad= input("İsim:")
    if ad in rehber:
        print("Telefon Numarası:", rehber.get(ad))
    print(rehber)
def sil():
    ad= input("İsim:")
    if ad in rehber:
        rehber.pop(ad)
        print(ad, " silindi...")
    else :
        print("Böyle bir kullanıcı yok!")
def liste():
    print("İsim      Numara")
    for x in rehber:
        print(x, rehber.get(x))
    print(len(rehber), "kişi listelendi")
while True:
    os.system('cls')
    print("""
    Telefon Rehberi
    Ekle -1
    Ara -2
    Sil -3
    Liste-4""")
    seç=input("Seçiminiz:")
    if seç == "1":
        ekle()
    elif seç == "2":
        ara()
    elif seç == "3":
        sil()
    elif seç == "4":
        liste() 
    input("Devam için enter...")
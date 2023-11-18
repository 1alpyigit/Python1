#def toplam(a, b):
#    return a + b
#print(toplam(5,3))

#def selam():
#    print("Merhaba!")
#selam()    


#def carpma(a, b):
#    return a*b

#while True :
#    sayı1 = float(input("Bir sayı gir: "))
#    sayi2 = float(input("ikinci sayıyı girin: "))

#    sonuç = carpma(sayı1, sayi2)
#    print("Çarpma sonucu: ", sonuç)
#    input("Devam etmek için enterla > ") 

##def mesaj_olustur(isim, mesaj):
##    return f"{isim}: {mesaj}"

##while True :
##    isim : str(input("Bir isim gir"))

## FONKSİYON ÖRNEKLER

#def faktoriyel(n):
#    if n == 0:
#        return 1
#    else:
#        return n * faktoriyel(n-1)
    
#sayi = int(input("Hanfi sayının faköriyeli hesaplansın: "))
#print(f"{sayi}! = {faktoriyel(sayi)}")

#def fibonacci(n):
#    if n <= 1:
#        return n
#    else :
#        return fibonacci(n-1) + fibonacci(n-2)
#while True:
#    sayı = int(input(" Kaçıncı terimini görmek istiyorsun fibonaccinin! "))
#    print(f"Fibonacci serisinin {sayı}, terim: {fibonacci(sayı)}")    
#    input("Deman etmek için enterle >|")

#def asal_mı(sayı):
#    if sayı <=1:
#        return False
#    for i in range(2, sayı):
#        if sayı % i == 0:
#            return False
#        return True
#while True:    
#    sayı = int(input("Bir sayı girin: "))
#    if asal_mı(sayı):
#        print(f"{sayı} asal bir sayırıdır! ")
#    else:
#        print(f"{sayı} asal bir sayı değildir.")
#    input("Tekrarsa ENTER Bas!")            

#def sayıuret():
#    import random
#    return random.randint(1,100)
#while True:
#    rasgele_sayı = sayıuret()
#    print("Üretilen sayı: ", rasgele_sayı)
#    input("Hoşuna gittiyse tekrar yapmak için enter!")


#rasgele slot

#import random
#def rasgelesayıuret(min_deger, max_deger, adet):
#    rasgelesayılar=[]
#    for i in range(adet):
#        rasgelesayı = random.randint(min_deger, max_deger)
#        rasgelesayılar.append(rasgelesayı)
#    return rasgelesayılar
#min_deger = 50
#max_deger = 1000
#adet = 5
#while True:
#    rasgelesayılar = rasgelesayıuret(min_deger, max_deger, adet)
#    print(f"{min_deger} ile {max_deger} arasında {adet} adet rasgele sayılar")
#    print(rasgelesayılar)
#    input("Zevk aldıysan entrla! 'Şans seninle'")

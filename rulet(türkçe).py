import random

def rulet():
    #Rulet tekerleği üzerindeki sayılar ve renkleri 
    sayilar=list(range(0,37))
    renkler={
        'kırmızı':[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36],
        'siyah':[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    }

    #Oyuncu başlangıç bakiyesi 
    bakiye=1000 

    while True:
        print("\n===Rulet Oyunu===")
        print(f"Bakiyeniz: {bakiye}")


        #Bahis miktarı 
        while True:
            try:
                bahis=int(input("Bahis miktarını giriniz(0 girilirse bahis biter): "))
                if bahis>=0 and bahis<=bakiye:
                    break 
                else:
                    print("Geçersiz bahis miktarı.Lütfen tekrar deneyiniz")
            except(ValueError,TypeError,SyntaxError):
                print("Bir hata oluştu")
        if bahis==0:
            print("Toplam bahis miktarı 0.Oyun sonlandırılıyor...")
            break 

        #Bahis menüsü 
        print("\nBahis Türleri: ")
        print("1-Tek sayı")
        print("2-Çift sayı")
        print("3-Kırmızı")
        print("4-Siyah")

        secim=input("Bahis türünü seçiniz(1-4): ")
        tekerlek=random.choice(sayilar)
        renk='kırmızı' if tekerlek in renkler["kırmızı"] else 'siyah' 
        print(f"Rulet tekerleği döndü ve durdu: {tekerlek} ({renk})")

        #Oyun kontrolü 
        if (secim=="1" and tekerlek%2==1) or (secim=="2" and tekerlek%2==0) or (secim=="3" and renk=='kırmızı') or (secim=="4" and renk=='siyah'):
            kazanc=bahis*2 
            bakiye+=kazanc 
            print(f"Tebrikler kazandınız.Kazanç: {kazanc}")
            print(f"Toplam bakiye: {bakiye}")
        else:
            print("Üzgünüm kaybettiniz :(")
            bakiye-=bahis 
        #bakiye kontrolü 
        if bakiye<=0:
            print("Bakiyeniz sıfırlandı.Oyun bitti...")
            break 


if __name__=="__main__":
    rulet() 




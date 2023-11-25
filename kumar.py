import random

print("1-Rulet Oynamak ")
print("2-İskambil Tahmin Oyunu ")
print("3-Barbut Oyunu ")

seçim =str(input("Hangi Oyunu Oynamak İstersiniz"))

#iskambil
class Kart:
    def __init__(self, isim, deger):
        self.isim = isim
        self.deger = deger

class IskambilOyunu:
    def __init__(self):
        self.destede_kartlar = []
        self.oyuncu_el = []
        self.bilgisayar_el = []

    def desteyi_olustur(self):
        kart_turleri = ["Karo", "Kupa", "Maça", "Sinek"]
        kart_degerleri = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Vale", "Kız", "Papaz"]

        for tur in kart_turleri:
            for deger in kart_degerleri:
                kart = Kart(f"{deger} {tur}", kart_degerleri.index(deger) + 1)
                self.destede_kartlar.append(kart)

    def desteyi_karistir(self):
        random.shuffle(self.destede_kartlar)

    def kart_dagıt(self):
        self.oyuncu_el.append(self.destede_kartlar.pop())
        self.bilgisayar_el.append(self.destede_kartlar.pop())

    def oyunu_oyna(self):
        self.desteyi_olustur()
        self.desteyi_karistir()

        for _ in range(2):
            self.kart_dagıt()

        while True:
            print("Oyuncu El:", [kart.isim for kart in self.oyuncu_el])
            secim = input("Başka bir kart çekmek istiyor musunuz? (Evet/Hayır): ").upper()

            if secim == "E":
                self.kart_dagıt()
            elif secim == "H":
                break
            else:
                print("Geçersiz bir seçim yaptınız. Lütfen 'E' veya 'H' girin.")

        while sum(kart.deger for kart in self.bilgisayar_el) < 17:
            self.kart_dagıt()

        print("Oyuncu El:", [kart.isim for kart in self.oyuncu_el])
        print("Bilgisayar El:", [kart.isim for kart in self.bilgisayar_el])

        toplam_oyuncu = sum(kart.deger for kart in self.oyuncu_el)
        toplam_bilgisayar = sum(kart.deger for kart in self.bilgisayar_el)

        if toplam_oyuncu > 21:
            print("Oyuncu Kaybetti. (Toplam Değer: {})".format(toplam_oyuncu))
        elif toplam_bilgisayar > 21:
            print("Oyuncu Kazandı. (Toplam Değer: {})".format(toplam_oyuncu))
        elif toplam_oyuncu > toplam_bilgisayar:
            print("Oyuncu Kazandı. (Toplam Değer: {})".format(toplam_oyuncu))
        elif toplam_bilgisayar > toplam_oyuncu:
            print("Oyuncu Kaybetti. (Toplam Değer: {})".format(toplam_oyuncu))
        else:
            print("Berabere. (Toplam Değer: {})".format(toplam_oyuncu))

#iskabil



#rulet
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

#rulet

#barbut

import random

def barbut_oyunu():
    print("Barbut Oyununa Hoş Geldiniz!")
    
    while True:
        input("Oynamak için bir tuşa basın...")
        
        oyuncu_zar = random.randint(1, 6)
        bilgisayar_zar = random.randint(1, 6)
        
        print(f"Siz {oyuncu_zar} attınız.")
        print(f"Bilgisayar {bilgisayar_zar} attı.")
        
        if oyuncu_zar > bilgisayar_zar:
            print("Tebrikler! Kazandınız.")
        elif oyuncu_zar < bilgisayar_zar:
            print("Maalesef kaybettiniz.")
        else:
            print("Berabere! Tekrar deneyin.")
        
        devam = input("Başka bir oyun oynamak ister misiniz? (Evet/Hayır): ")
        if devam.lower() != 'evet':
            break

    print("Oyunu kapattınız. İyi günler!")

#barbut


if seçim == "3":
    if __name__=="__main__":
        barbut_oyunu()

if seçim == "1":
    if __name__=="__main__":
        rulet() 

if seçim == "2":
    if __name__ == "__main__":
        oyun = IskambilOyunu()
        oyun.oyunu_oyna()

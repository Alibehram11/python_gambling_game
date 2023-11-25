import random

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


if __name__ == "__main__":
        oyun = IskambilOyunu()
        oyun.oyunu_oyna()

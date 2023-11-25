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

from sarki import *
import time

print("""**************************
Hos geldiniz...
**************************
1 - Sarki Ekle
2 - Sarki Sil
3 - Toplam Sarki Suresi
4 - Tum Sarkilari Goster
q - Cikis
**************************""")

sarkiClass = Fonksiyonlar()

while (True):
    islem = input("Yapacaginiz islem: ")

    if (islem == "q"):
        print("Program sonlandiriliyor...")
        break

    elif (islem == "1"):
        sarkiIsmi = input("Sarki Ismi: ")
        sarkici = input("Sarkici: ")
        album = input("Album: ")
        produksiyonSirket = input("Produksiyon Sirket: ")
        sarkiSuresi = int(input("Sarki Suresi: "))

        yeniSarki = SarkiVeSarkici(sarkiIsmi, sarkici, album, produksiyonSirket, sarkiSuresi)

        print("Sarki ekleniyor...")
        sarkiClass.sarkiEkle(yeniSarki)
        time.sleep(2)
        print("Sarki eklendi...")

    elif (islem == "2"):
        isim = input("Hangi sarki: ")
        print("Sarki siliniyor...")
        sarkiClass.sarkiSil(isim)
        time.sleep(2)
        print("Sarki silindi...")

    elif (islem == "3"):
        sarkiClass.toplamSarkiSuresi()

    elif (islem == "4"):
        sarkiClass.sarkilariGoster()

    else:
        print("Hatali tuslama yapildi... Tekrar deneyin.")
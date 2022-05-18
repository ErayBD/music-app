import sqlite3

class SarkiVeSarkici():

    def __init__(self, sarkiIsim, sarkici, album, produksiyonSirket, sarkiSuresi) -> None:
        self.sarkiIsim = sarkiIsim
        self.sarkici = sarkici
        self.album = album
        self.produksiyonSirket = produksiyonSirket
        self.sarkiSuresi = sarkiSuresi

    def __str__(self) -> str:
        return ("Sarki Ismi: {}\nSarkici: {}\nAlbum: {}\nProduksiyon Sirket: {}\nSarki Suresi: {}".format(self.sarkiIsim, self.sarkici, self.album, self.produksiyonSirket, self.sarkiSuresi))

class Fonksiyonlar():

    def __init__(self) -> None:
        self.baglantiKur()

    def baglantiKur(self):
        self.baglanti = sqlite3.connect("C:/Users/Eray/Desktop/Coding/Languages/Python/sarkiDataBase/repertuvar.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table if not exists sarkilar (sarkiIsim TEXT, sarkici TEXT, album TEXT, produksiyonSirket TEXT, sarkiSuresi INT)"

        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiKes(self):
        self.baglanti.close()

    def sarkiEkle(self, sarki):
        sorgu = "Insert into sarkilar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu, (sarki.sarkiIsim, sarki.sarkici, sarki.album, sarki.produksiyonSirket, sarki.sarkiSuresi))
        self.baglanti.commit()
    
    def sarkiSil(self, sarkiIsim):
        sorgu = "Delete from sarkilar where sarkiIsim = ?"
        self.cursor.execute(sorgu, (sarkiIsim, ))
        self.baglanti.commit()

    def sarkilariGoster(self):
        sorgu = "Select * from sarkilar"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()

        if (len(sarkilar) == 0):
            print("Sarki bulunmuyor...")
        
        else:
            sarkiNumarasi = 0
            for i in sarkilar:
                sarkiNumarasi += 1
                print("\nSarki Numarasi: {}:\n".format(sarkiNumarasi))
                sarki = SarkiVeSarkici(i[0], i[1], i[2], i[3], i[4])
                print(sarki,"\n")
        

    def toplamSarkiSuresi(self):
        sorgu = "SELECT SUM(sarkiSuresi) FROM sarkilar"
        self.cursor.execute(sorgu)
        result = self.cursor.fetchone()[0]
        print("Toplam sarki suresi: {}".format(result))

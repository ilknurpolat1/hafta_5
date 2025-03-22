class Hesap:
    def __init__(self, sayı1, sayı2):
        self.sayı1 = sayı1
        self.sayı2 = sayı2

    def carp(self):
        sonuc=self.sayı1 * self.sayı2
        return sonuc
    def bol(self):
        sonuc= self.sayı1 / self.sayı2
        return sonuc
    def topla(self):
        sonuc=self.sayı1 + self.sayı2
        return sonuc
    def cıkar(self):
        sonuc=self.sayı1 - self.sayı2
        return sonuc


    def yazdır(self):
     toplam=self.topla()
     carpma=self.carp()
     bolme=self.bol()
     cıkarma=self.cıkar()

     print('sayıların toplamı:',toplam)
     print('sayıların çarpımı:', carpma)
     print('sayıların bölmesi:', bolme)
     print('sayıların çıkarılması:', cıkarma)


K= Hesap(10, 5)
K.yazdır()
K.topla()
K.cıkar()
K.bol()
K.carp()



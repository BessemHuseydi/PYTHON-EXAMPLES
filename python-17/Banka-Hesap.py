class BankaHesapi:
    def __init__(self,isim,bakiye=0):
        self.isim=isim
        self.bakiye=bakiye
        print(f"Hesapiniz olusturdu sayin {self.isim}")
    def para_yatir(self,miktar):
        if miktar>0:
            self.bakiye+=miktar
            return f"{miktar} TL yatiridi . Yeni bakiye :{self.bakiye}"
        return "Gecersiz yatirim miktari"
    def para_cek(self, miktar):
        if 0 < miktar <= self.bakiye:
            self.bakiye -= miktar
            return f"{miktar} TL çekildi. Yeni bakiye: {self.bakiye}"
        return "Geçersiz çekim miktari veya yetersiz bakiye"


# Örnek kullanım
hesap = BankaHesapi("Ahmet Kaya", 1000)
print(hesap.para_yatir(500))  # 500 TL yatır
print(hesap.para_cek(200))    # 200 TL çek
print(hesap.bakiye)           # Bakiyeyi göster

class Arac:
     # Arac sınıfı, tüm araçların temelini oluşturur
    def __init__(self,marka, model):
        self.marka=marka
        self.model=model 

    def bilgi_goster(self):
    # Araç bilgilerini gösterir
        return f"Marka : {self.marka}, Model : {self.model}"

class Araba(Arac):
     # Araba sınıfı, Arac sınıfından türetilmiştir ve kapı sayısını ekler
    def __init__(self, marka, model,kapi_sayisi):
        super().__init__(marka, model)
        self.kapi_sayisi=kapi_sayisi

    def bilgi_goster(self):
      # Araba bilgilerini, kapı sayısı ile birlikte gösterir
        return f"Marka : {self.marka}, Model : {self.model}, Kapi Sayisi: {self.kapi_sayisi}\n"




# Toyota Corolla, 4 kapılı
araba1 = Araba("Toyota", "Corolla", 4)
print(araba1.bilgi_goster())

# Ford Mustang, 2 kapılı
araba2 = Araba("Ford", "Mustang", 2)
print(araba2.bilgi_goster())

# Mercedes-Benz C Class, 4 kapılı
araba3 = Araba("Mercedes-Benz", "C Class", 4)
print(araba3.bilgi_goster())

# BMW 3 Serisi, 4 kapılı
araba4 = Araba("BMW", "3 Serisi", 4)
print(araba4.bilgi_goster())
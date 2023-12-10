def us_alma(x, y):
    sonuc = x ** y
    return sonuc

# Kullanıcıdan x ve y değerlerini al
print ("birinci girilen sayi taban sayisi, ikinci sayi ise ust olacaktir ")
x = float(input("Lütfen x değerini girin: "))
y = float(input("Lütfen y değerini girin: "))

# Fonksiyonu çağırıp sonucu yazdır
sonuc = us_alma(x, y)
print(f"{x} üzeri {y} = {sonuc}")
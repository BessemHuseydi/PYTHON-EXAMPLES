def ozyineleme(array, uzunluk):
    if uzunluk < 0:
        return 0
    else:
        if array[uzunluk] % 2 == 1:
            toplam = array[uzunluk] * 4 + 5
        else:
            toplam = array[uzunluk] * 3 + 2
        return toplam + ozyineleme(array, uzunluk - 1)

liste = [2, 4, 7, 12, 15, 21, 34, 42, 51, 63]
dizi_uzunlugu = len(liste) - 1

sonuc = ozyineleme(liste, dizi_uzunlugu)
print("Tek sayıları 4 katının 5 fazlası, çift sayıların 3 katının 2 fazlasını yapan özyineleme fonksiyonu\n")
print(f"Sonuç: {sonuc}")

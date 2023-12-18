def hanoi_kuleleri(n, kaynak, hedef, yaradimci):
    if n == 1:
        print(f"Disk 1'i {kaynak} çubuğundan {hedef} çubuğuna taşı")
        return
    hanoi_kuleleri(n - 1, kaynak, yaradimci, hedef)
    print(f"Disk {n}'i {kaynak} çubuğundan {hedef} çubuğuna taşı")
    hanoi_kuleleri(n - 1, yaradimci, hedef, kaynak)

def kullanici_girdisi_al():
    while True:
        try:
            n = int(input("Hanoi Kuleleri için 100'den küçük, pozitif bir disk sayısı girin: "))
            if n <= 0 or n >= 10:
                print("Hatali degerler girdiniz veya [TASMA]")
            else:
                return n
        except ValueError:
            print("Geçersiz girdi. Lütfen bir tam sayı girin.")

# Kullanıcıdan disk sayısını alma
n = kullanici_girdisi_al()

# Hanoi Kuleleri bulmacasını çözme
hanoi_kuleleri(n, 'A', 'C', 'B')  # A: Kaynak Çubuk, C: Hedef Çubuk, B: Yardımcı Çubuk

# 0 ile 100 arasındaki tek sayıları ekrana yazdır
def tekleri_yazdir(x,y):
    if x%2==1:
        for i in range(x, y, 2):
          print(i)
    else:
       tekleri_yazdir(x+1,y)

print("iki sayi arasindaki tek sayilari bulan fonksiyon")

number1=int(input("birinci sayiyi giriniz  :"))
number2=int(input("ikinci sayiyi giriniz  :"))

sonuc=tekleri_yazdir(number1,number2)

print(f"sayilari {sonuc}")
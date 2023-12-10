def asal_mi(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
        
    return True  
number=int(input("bir sayi giriniz : "))

if asal_mi(number):
    print(f"{number} asal bir sayidir .")
else:
     print(f"{number} asal bir sayi degildir .")
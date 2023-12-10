def factorial_calculate(x):
    if x < 0:
        return "Negatif sayilarin faktöriyeli hesaplanamaz."
    elif x==0 or x==1:
        return 1
    else:
        return x*factorial_calculate(x-1)
    
# Kullanıcıdan bir sayı al 
number=int(input("Faktöriyeli hesaplanacak sayiyi giriniz: "))

factorial=factorial_calculate(number)
print(" ")
print(f"{number}! = {factorial}")
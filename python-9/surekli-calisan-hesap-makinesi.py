while True :
    print("---------------------------------Hesap Makinesi----------------------------------------\n\n\n")
    islem=input("yapnmak istediginiz islemi | + , - , * , / , % |  islemi giriniz  cikis icin|N,n| basiniz :\n")
    
    if (islem == 'n' or islem == 'N'):
        print("Hesap makinsinde cikis yapiliyor --->   :)\n ")
        break
    
    try:
        number1=float(input("Birinci sayi giriniz  :"))
        
        number2=float(input("Ikinci sayi giriniz  :"))

    except ValueError:
        print("Lütfen geçerli bir sayi girin")
        continue  
    if(islem=='+'):
        sonuc=number1+number2 
    elif(islem=='-'):
        sonuc=number1-number2
    elif(islem=='*'):
        sonuc=number1*number2
    elif islem == '/':
        if number2 != 0:
            sonuc = number1 / number2
        else:
            print("Bir sayi sifira bölünemez!")
            continue
    elif(islem=='%'):
        sonuc=number1%number2

    else:
        print("Geçersiz işlem.")
        continue

    print(f"islem sonucu  ={sonuc}")
def binary_search(array, target):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Eleman bulunamadı

# Kullanım örneği
sorted_list = [2, 4, 7, 12, 15, 21, 34, 42, 51, 63]

try:
    target_value = int(input("Aramak istediğiniz sayıyı giriniz: "))
    result = binary_search(sorted_list, target_value)
    if result != -1:
        print(f"{target_value} hedef değeri indeksi: {result}")
    else:
        print(f"{target_value} hedef değeri bulunamadı.")
except ValueError:
    print("Lütfen geçerli bir sayi giriniz.")

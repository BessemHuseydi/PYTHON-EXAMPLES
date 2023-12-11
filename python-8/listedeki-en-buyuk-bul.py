def find_max_number(numbers):
    max_number = numbers[0]

    for num in numbers:
        if num > max_number:
            max_number = num

    return max_number

# Örnek kullanım:
number_list = [3, 7, 1, 15, 9, 5]
max_num = find_max_number(number_list)
print(f"Listedeki en büyük sayı: {max_num}")

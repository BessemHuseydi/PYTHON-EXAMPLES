def bubble_sort(array):
    length = len(array)

    for i in range(length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

liste = [0, 15, 18, 68, 100, 15278, 120, 12, 33, 685, 101]
bubble_sort(liste)
print("Siralanmiş Liste:", liste)

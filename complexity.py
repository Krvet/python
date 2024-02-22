# Сортировка пузырьком, сложность О(n^2), имеет два цикла for, что при больших данных имеет большее значение чем остальное.

def bubbleSort(array):
    swapped = False
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped= True
        if swapped:
            swapped=False
        else:
            break
    return array

# Сортировка выбором, сложность О(n^2), имеет два цикла for, что при больших данных имеет большее значение чем остальное.

def selectionSort(array):
    for i in range(len(array)-1):
        min_idx = i
        for idx in range(i + 1, len(array)-1):
            if array[idx] < array[min_idx]:
                min_idx = idx
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

# Сортировка вставками, сложность О(n^2), имеет два цикла for и while, что при больших данных имеет большее значение чем остальное.

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while array[j] > key and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

# Сортировка Шелла, сложность О(n^2), имеет три цикла for и два while,/ while interval > 0:/не играет большой роли поэтому в сложность не учитывается
import math

def shellSort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k -1
    return array
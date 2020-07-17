#!/usr/bin/env python3

# Selection Sort
def selection_sort(array):
    for i in range(len(array)-1):                       
        minIndex = i
        for j in range(i, len(array)):
            if array[minIndex] > array[j]:
                minIndex = j
        array[minIndex], array[i] = array[i], array[minIndex]

array = [12, 54, 23, 33, 67, 45, 55, 23, 48]
print("Array before sorting")
print(array)
selection_sort(array)
print("Array after sorting")
print(array)
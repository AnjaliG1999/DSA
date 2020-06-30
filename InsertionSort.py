#!/usr/bin/env python3

# Insertion Sort
def insertion_sort(array):
    for j in range(1,len(array)):     # array[1..j-1] represents the sorted array
        key = array[j]

        # insert array[j] into the sorted sequence array[1..j-1]
        i = j-1
        while i > 0 and array[i] > key:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = key

array = [12, 54, 23, 33, 67, 45, 55, 23, 48]
print("Array before sorting")
print(array)
insertion_sort(array)
print("Array after sorting")
print(array)
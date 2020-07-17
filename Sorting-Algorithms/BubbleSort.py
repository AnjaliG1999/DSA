#!/usr/bin/env python3

# Bubble Sort
def bubble_sort(array):
    for i in range(len(array)-2):                       # executed n-1 times, n=length of the array
        for j in range(1, len(array), i+1)[::-1]:       # for j = A.length downto i+1
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]

array = [12, 54, 23, 33, 67, 45, 55, 23, 48]
print("Array before sorting")
print(array)
bubble_sort(array)
print("Array after sorting")
print(array)
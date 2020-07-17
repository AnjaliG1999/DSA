#!/usr/bin/env python3

# merging 2 sorted arrays
def merge(array, lowIndex, midIndex, highIndex):
    len1 = midIndex - lowIndex + 1
    len2 = highIndex - midIndex
    leftArray = [0] * len1
    rightArray = [0] * len2

    # populate the 2 arrays: left and right
    for i in range(len1):
        leftArray[i] = array[lowIndex + i]

    for j in range(len2):
        rightArray[j] = array[midIndex + j + 1]

    i = j = 0

    # Merging the elements of the sorted arrays: method 1
    
    # Saving the last element of the arrays as Infinity
    leftArray[len1-1] = float('inf')
    rightArray[len2-1] = float('inf')

    while i < len1-1 or j < len2-1:
        if leftArray[i] <= rightArray[j]:
            array[k] = leftArray[i]
            i += 1
        else:
            array[k] = rightArray[j]
            j += 1
        k += 1

    # Merging the elements of the sorted arrays: method 2
    # Uncomment the code below to use the second method
    '''
    k = lowIndex
    # Copy the elements in a sorted manner
    while i < len1 and j < len2:       
        if leftArray[i] <= rightArray[j]:
            array[k] = leftArray[i]
            i += 1
        else:
            array[k] = rightArray[j]
            j += 1
        k += 1
    
    # Copy the remaining elements in the array
    while i < len1:
        array[k] = leftArray[i]
        i += 1
        k += 1

    while j < len2:
        array[k] = rightArray[j]
        j += 1
        k += 1
    '''
#-----------function merge() ends here----------------------------

# Merge Sort
def merge_sort(array, lowIndex, highIndex):
    if lowIndex < highIndex:
        midIndex = (lowIndex + (highIndex - 1) )//2

        merge_sort(array, lowIndex, midIndex)
        merge_sort(array, midIndex + 1, highIndex)
        merge(array, lowIndex, midIndex, highIndex)

array = [12, 54, 23, 33, 67, 45, 55, 23, 48]
print("Array before sorting")
print(array)
merge_sort(array, 0, len(array)-1)
print("Array after sorting")
print(array)
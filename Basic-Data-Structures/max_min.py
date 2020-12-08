def findMinIterative(arr):
    minimum = arr[0]

    for index in range(1, len(arr)):
        if minimum > arr[index]:
            minimum = arr[index]        
    return minimum

def findMaxIterative(arr):
    maximum = arr[0]

    for index in range(1, len(arr)):
        if maximum < arr[index]:
            maximum = arr[index]
    return maximum        

def findMinRecursive(arr, n):
    return arr[0] if n==1 else min(findMinRecursive(arr[1:], n-1), arr[0])

def findMaxRecursive(arr, n):
    return arr[0] if n==1 else max(findMaxRecursive(arr[1:], n-1), arr[0])

def findMinLibrary(arr):
    return min(arr)

def findMaxLibrary(arr):
    return max(arr)

arr = [1, 4, 6, 4, 6, 2, 7]
# minVal = findMinIterative(arr)
# maxVal = findMaxIterative(arr)

# minVal =findMinRecursive(arr, len(arr))
# maxVal = findMaxRecursive(arr, len(arr))

minVal = findMinLibrary(arr)
maxVal = findMaxLibrary(arr)

print("Minimum: {0}, Maximum: {1}".format(minVal, maxVal))
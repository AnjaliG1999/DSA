def findDuplicates(arr):
    dict = {}
    duplicates = set()
    for val in arr:
        if val in dict:
            duplicates.add(val)
        else:
            dict[val] = True
    return duplicates

def findDuplicates2(arr):
    duplicates = []
    n = len(arr)
    for i in arr:
        arr[i%n] += n
    
    for i in range(n):
        if arr[i] > 2*n:
            duplicates.append(i)
    return duplicates

arr = [1, 2, 3, 6, 3, 6, 1, 1]
duplicates = findDuplicates(arr)
# duplicates = findDuplicates2(arr)

print("Array: {}".format(arr))
if len(duplicates):
    print("Duplicate elements in the array: {}".format(duplicates))
else:
    print("There is no duplicate element in the array")
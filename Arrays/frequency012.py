def frequency1(arr):
    n = len(arr)
    count = [0, 0, 0]

    for key in arr:
        count[key] += 1

    for val in range(count[0]):
        arr[val] = 0
    
    for val in range(count[0], count[1]+count[0]):
        arr[val] = 1
    
    for val in range(count[1]+count[0], n):
        arr[val] = 2

    return arr

def frequency2(arr):
    index = 0
    sortedArr = []

    for key in arr:
        if key == 2:
            sortedArr.append(key)
        elif key == 1:
            sortedArr.insert(index, key)
            index += 1
        else:
            sortedArr.insert(0, key)
            index += 1

    return sortedArr

def dutchNationalFlagAlgo(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# print(frequency1(arr))
print(frequency2(arr))
# print(dutchNationalFlagAlgo(arr))
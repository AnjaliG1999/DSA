def shiftNegatives(arr):
    left = 0
    right = len(arr)-1

    while left <= right:
        if arr[left] < 0:
            left += 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        
    return arr

def quicksortPartition(arr):
    left = 0
    for curr in range(len(arr)):
        if arr[curr] < 0:
            arr[left], arr[curr] = arr[curr], arr[left]
            left += 1
    
    return arr
        
arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
# print(shiftNegatives(arr))
print(quicksortPartition(arr))
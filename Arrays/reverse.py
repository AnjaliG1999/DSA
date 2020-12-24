def reverseIterative(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr

def reverseRecursive(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverseRecursive(arr, start+1, end-1)
    return arr

def reverseList(arr):
    return arr[::-1]

arr = [1, 2, 3, 4, 5, 6, 7]
print("Array: {}".format(arr))

# revArray = reverseIterative(arr)
revArray = reverseRecursive(arr, 0, len(arr)-1)
# revArray = reverseList(arr)

print("Reversed array: {}".format(revArray))
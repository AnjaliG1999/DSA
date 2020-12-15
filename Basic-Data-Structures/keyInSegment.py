def isPresent(arr, k, x, n):
    i=0
    while i < n:
        j=0
        while j < k:
            if arr[i+j] == x:
                break
            j += 1

        if j == k:
            return False
        
        i += k

    if i == n:
        return True
    
    j = i - k

    while j < n:    
        if x == arr[j]:
            break
        j += 1
    if j == n:
        return False

arr = [3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3, 4, 8]
n = len(arr)
x, k = 3, 3

res = isPresent(arr, k, x, n)
print(res)
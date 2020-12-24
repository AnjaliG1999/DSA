def isPresent(arr, k, x, n):
    i=0
    while i < n//k:
        j=0
        while j < k:
            if arr[k*i+j] == x:
                break
            j += 1

        if j == k:
            return False
        
        i += 1

    if k*i == n:
        return True

    for j in range(k*i+1, n):   
        if x == arr[j]:
            return True
    return False

arr = [3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3, 4, 3]
n = len(arr)
x, k = 3, 3

if isPresent(arr, k, x, n):
    print('{} is present in every segment of size {}'.format(x, k))
else:
    print('{} is not present in every segment of size {}'.format(x, k))
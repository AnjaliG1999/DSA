def missingInteger(arr, n):
    naturalSum = (n) * (n+1) // 2
    missing = naturalSum - sum(arr)
    return missing

def missingIntegerModified(arr, n):
    total = 1
    for i in range(2, n+2):
        total += i
        total -= arr[i-2]
    return total

def missingIntegerBit(arr, n):
    x1 = arr[0]
    x2 = 1
    for i in range(1, n):
        x1 ^= arr[i]
    
    for i in range(2, n+2):
        x2 ^= i
    
    return x1 ^ x2

arr = [1, 2, 4, 6, 3, 7, 8]
n = len(arr)
print("Integers: {}".format(arr))
# missingNo = missingInteger(arr, n+1)
# missingNo = missingIntegerModified(arr, n)
missingNo = missingIntegerBit(arr, n)
print("Missing number: {}".format(missingNo))
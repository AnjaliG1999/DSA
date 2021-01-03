def getPairsCount(arr, sum):
    count = 0
    viewed = [0] * 150
    for val in arr:
        viewed[val] += 1
    
    for val in arr:
        count += viewed[sum - val]

        if(sum - val == val):
            count -= 1
        
    return count//2

def getPairsCountBrute(arr, sum):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                count += 1
    return count

arr = [1, 5, 7, -1, 5]
sum = 6
# pairs = getPairsCount(arr, sum)
pairs = getPairsCountBrute(arr, sum)
print("There are {} pairs in the array with the sum {}".format(pairs, sum))
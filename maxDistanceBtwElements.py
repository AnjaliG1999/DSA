#!usr/bin/env python3

# Find the maximum distance between two occurrences of same element in array
arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]

hashMap = {}
max_dist = 0
for index in range(len(arr)):
    value = arr[index]
    if value not in hashMap:
        hashMap[value] = index
    else:
        max_dist = max(max_dist, index - hashMap[value])
    
print(max_dist)
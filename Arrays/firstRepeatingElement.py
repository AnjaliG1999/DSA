def firstRepeatedHashMap(arr):
    elements = {}
    for val in arr:
        elements[val] = elements.get(val, 0) + 1

    for key in arr:
        if elements[key] > 1:
            return [arr.index(key), key]
    return [-1, -1]

def firstRepeated(arr):
    minIndex = -1
    elements = {}
    for i in range(len(arr)-1, -1, -1):
        if arr[i] in elements:
            minIndex = i
        else:
            elements[arr[i]] = True
    return [minIndex, arr[minIndex]]

arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]
firstIndex, first = firstRepeated(arr)
if firstIndex == -1:
    print("There are no repeating elements")
else:
    print("The first repeating element is {} at index {}".format(first, firstIndex))
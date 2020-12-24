dict = {}

def findFrequency(arr):
    global dict
    for key in arr:
        dict[key] = [dict.get(key, 0) + 1]
    
def frequency1(arr, val): 
    findFrequency(arr)   
    return dict[val] if val in dict else 0

def frequency2(arr, val):
    count = 0
    for key in arr:
        if key == val:
            count += 1
    return count

arr = [1, 3, 5, 3, 6, 7, 1, 0, 3]
val = int(input('Enter value to count: '))
# freq = frequency1(arr, val)
freq = frequency2(arr, val)
print("No. of {}'s in array: {}".format(val, freq))
def nearestSmallerElementRight(arr):
    stack = []
    output = [None] * n

    for i in range(n-1, -1, -1):
        while (len(stack)!=0) and (arr[i] <= stack[-1]):
            stack.pop()
        if len(stack)==0:
            output[i] = -1
        else:
            output[i] = stack[-1]
        stack.append(arr[i])
    
    return output

def nearestSmallerElementLeft(arr):
    stack = []
    output = [None] * n

    for i in range(n):
        while (len(stack)!=0) and (arr[i] <= stack[-1]):
            stack.pop()
        if len(stack)==0:
            output[i] = -1
        else:
            output[i] = stack[-1]
        stack.append(arr[i])
    
    return output

arr = [10, 5, 11, 6, 20, 12]
n = len(arr)

ngeRight = nearestSmallerElementRight(arr)
ngeLeft = nearestSmallerElementLeft(arr)

print("The next greatest elements of {} to right are {}".format(arr, ngeRight))
print("The next greatest elements of {} to left are {}".format(arr, ngeLeft))
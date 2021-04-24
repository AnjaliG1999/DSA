def nearestSmallerElementRight(arr, n):
    stack = []
    output = [None] * n

    for i in range(n-1, -1, -1):
        while (len(stack)!=0) and (arr[i] <= stack[-1][0]):
            stack.pop()
        if len(stack)==0:
            output[i] = n
        else:
            output[i] = stack[-1][1]
        stack.append([arr[i], i])
    
    return output

def nearestSmallerElementLeft(arr, n):
    stack = []
    output = [None] * n

    for i in range(n):
        while (len(stack)!=0) and (arr[i] <= stack[-1][0]):
            stack.pop()
        if len(stack)==0:
            output[i] = -1
        else:
            output[i] = stack[-1][1]
        stack.append([arr[i], i])
    
    return output

def maxAreaHistogram(arr, n):
    right = nearestSmallerElementRight(arr, n)
    left = nearestSmallerElementLeft(arr, n)
    width = [None] * n

    for i in range(n):
        width[i] = right[i] - left[i] -1
        width[i] *= arr[i]
    return max(width)

arr = [6, 2, 5, 4, 5, 1, 6]
n = len(arr)

mah = maxAreaHistogram(arr, n)
print("Maximum area for histogram {} is {}".format(arr, mah))

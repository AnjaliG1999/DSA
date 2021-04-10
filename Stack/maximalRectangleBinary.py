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

def maxRectangleBinary(matrix, n):
    maxm = 0
    arr = [0] * n

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 0:
                arr[col] = 0
            else:
                arr[col] += matrix[row][col]
        maxm = max(maxm, maxAreaHistogram(arr, n))
    return maxm

matrix = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]

maxArea = maxRectangleBinary(matrix, len(matrix))
print('Max Area of Binary Rectangle is: {}'.format(maxArea))
def stockSpanProblem(arr, n):
    stack = []
    output = [None] * n

    for i in range(n):
        while (len(stack)!=0) and (arr[i] >= stack[-1][0]):
            stack.pop()
        if len(stack)==0:
            output[i] = -1
        else:
            output[i] = stack[-1][1]
        stack.append([arr[i], i])
    
    for i in range(n):
        output[i] = i-output[i]
        
    return output


arr = [100, 80, 60, 70, 60, 75, 85]
n = len(arr)
span = stockSpanProblem(arr, n)
print("Stock spans for {} are {}".format(arr, span))
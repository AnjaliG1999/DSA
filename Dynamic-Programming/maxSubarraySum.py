def maxSubarrayCubic(arr, n):
    maxSum = -9999

    for left in range(n):
        for right in range(left, n):
            window_sum = 0

            for el in range(left, right+1):
                window_sum += arr[el]
            
            if window_sum > maxSum:
                maxSum = window_sum
    return maxSum

def maxSubarrayQuadratic(arr, n):
    maxSum = -9999

    for left in range(n):
        running_sum = 0
        for right in range(left, n):
            running_sum += arr[right]
        
            maxSum = max(maxSum, running_sum)

    return maxSum

def maxSubarrayLinear(arr, n):   
    maxSum = arr[0]
    running_sum = arr[0]

    for idx in range(1, n):
        running_sum = max(running_sum + arr[idx], arr[idx])
        maxSum = max(maxSum, running_sum)
        
    return maxSum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
# maxSum = maxSubarrayCubic(arr, n)
# maxSum = maxSubarrayQuadratic(arr, n)
maxSum = maxSubarrayLinear(arr, n)
print(maxSum)
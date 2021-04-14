def trappingRainWater(arr, n):
    height = 0
    water = 0

    for i in range(1, n-1):
        height = min(max(arr[i:]), max(arr[:i+1]))
        water += height - arr[i]
    return water

arr   = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
level = trappingRainWater(arr, len(arr))
print("Maximum water that can be accumulated is {} units".format(level))
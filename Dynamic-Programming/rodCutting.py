#!usr/bin/env python3

# Bottom-up approach
def bottomUpCutRod(price, size):
    optimal_price = [0 for i in range(size + 1)]
    for j in range(1, size + 1):
        revenue = -1
        for i in range(j):
            # find the maximum possible revenue
            revenue = max(revenue, price[i] + optimal_price[j-i-1])
        optimal_price[j] = revenue
    return optimal_price

# Memomized approach
def memoizedCutRodUtil(price, size, optimal_price):
    # return the maximum possible revenue
    if optimal_price[size] >= 0:
        return optimal_price[size]
    
    if not size:
        return 0
        
    revenue = -1
    for i in range(size):
        revenue = max(revenue, price[i] + memoizedCutRodUtil(price, size-i-1, optimal_price))
    optimal_price[size] = revenue
    return revenue

def memoizedCutRod(price, size):
    optimal_price = [-1 for i in range(size + 1)]
    return memoizedCutRodUtil(price, size, optimal_price)

price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
for size in range(11):
    # uncomment to find solution using tabular approach
    '''optimal_price = bottomUpCutRod(price, size)
    print("size " + str(size) + " -> " + str(optimal_price[size]))'''
    
    # to find solution using tabular approach
    print("size " + str(size) + " -> " + str(memoizedCutRod(price, size)))
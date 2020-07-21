#!usr/bin/env python3

# Find the number of unique BSTs possible with the given number of nodes

# Recursive function
def uniqueBSTrec(num):
    if num < 1:
        return 1

    catalan = 0
    for i in range(num):
        catalan += uniqueBSTrec(i) * uniqueBSTrec(num - i - 1)
    return catalan

# Iterative function
def uniqueBSTiter(num):
    if num <= 1:
        return 1
        
    catalan = [0 for i in range(num+1)]
    catalan[0] = catalan[1] = 1
    for i in range(2, num+1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]
    
    return catalan[-1]

nodes = int(input('Enter a number: '))
print('By recursive function: ' + str(uniqueBSTrec(nodes)))
print('By iterative function: ' + str(uniqueBSTiter(nodes)))
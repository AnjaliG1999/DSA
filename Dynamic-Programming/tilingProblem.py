#!usr/bin/env python3

''' The problem is solved by fibonacci series '''

def waysToTile1(n):
    '''
    count number of ways to tile a floor of size 2 x n using 2 x 1 tiles

    :params: n: int, width of the floor
    :rtype: int
    '''

    if n == 0 or n == 1:
        return n
    
    table = [0 for i in range(n+1)]
    table[1] = 1
    for val in range(2, n+1):
        table[val] = table[val-1] + table[val-2]
    return table[n]

def waysToTile2(n, m):
    '''
    count number of ways to tile a floor of size n x m using 1 x m tiles

    :params: n: int, length of the floor
             m: int, width of the floor
    :rtype: int
    '''

    if n < m:
        return 1
    
    if n == m:
        return 2
    
    table = [0 for i in range(n+2)]
    table[1] = 1
    for val in range(2,n+2):
        table[val] = table[val-1] + table[val-m]
    return table[n+1]

print('Ways to tile the floor:')
print('2 x 1 tiles: {}, n x m tiles: {}'.format(waysToTile1(5), waysToTile2(5,2)))
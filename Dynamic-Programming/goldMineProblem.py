#!usr/bin/env python3

"""Find out maximum amount of gold the miner can collect from the gold mine"""

# Helper function for recursive approach
def findMaxGoldRec(prevRow, prevCol):
    """
    :param: prevRow: int, previous row considered
            prevCol: int, previous column considered
    :rtype: int
    """
    if prevCol >= cols: return 0
    
    if prevRow >= rows or prevRow < 0: return 0
    
    upRight = findMaxGoldRec(prevRow-1, prevCol+1)
    right = findMaxGoldRec(prevRow, prevCol+1)
    downRight = findMaxGoldRec(prevRow+1, prevCol+1)
    return GoldMine[prevRow][prevCol] + max(upRight, right, downRight)

# Recursive approach: O(3^rows)
def findMaxGold(GoldMine):
    """
    :param: GoldMine: list[list[int]], matrix containing the amount of gold for each block
    :rtype: int
    """
    maxGold = 0
    for i in range(rows):
        g = findMaxGoldRec(i, 0)
        if g > maxGold:
            maxGold = g
    return maxGold
    
# Dynamic approach: O(rows*cols)  
def findMaxGoldDP(GoldMine, rows, cols):
    """
    :param: GoldMine: list[list[int]], matrix containing the amount of gold for each block
            rows: int, number of rows in the matrix
            cols: int, number of columns in the matrix
    :rtype: int
    """
    maxGold = [[0 for i in range(cols)] for j in range(rows)]
    for prevCol in range(cols-1, -1, -1):
        for prevRow in range(rows):
            # conditions to find values for the 3 possible paths from 
            # the previous cell: right and up, right, right and down
            if prevCol == cols-1:
                right = 0
            else:
                right = maxGold[prevRow][prevCol+1]
            
            if prevRow == 0 or prevCol == cols-1:
                rightUp = 0
            else:
                rightUp = maxGold[prevRow-1][prevCol+1]
                
            if prevRow == rows-1 or prevCol == cols-1:
                rightDown = 0
            else:
                rightDown = maxGold[prevRow+1][prevCol+1]
            
            maxGold[prevRow][prevCol] = GoldMine[prevRow][prevCol] + max(rightUp, right, rightDown)
            
    g = maxGold[0][0]
    for i in range(rows):
        g = max(g, maxGold[i][0])
    return g

GoldMine = [
    [1,3,1,5],
    [2,2,4,1],
    [5,0,2,3],
    [0,6,11,2]
]
rows = len(GoldMine)
cols = len(GoldMine[0])
print('Maximum gold that can be dug: ')
print('(Using recursion) ' + str(findMaxGold(GoldMine)))
print('(Using dynamic programming) ' + str(findMaxGoldDP(GoldMine, rows, cols)))
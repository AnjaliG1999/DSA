#!usr/bin/env python3

"""
Find the number of ways of making change for a particular number of units using the given types of coins

:param: coins: list, All the coin values available
		length: int, Length of the current coin list
		amount: int, Total amount for which change is to be calculated
:rtype: int
"""

# Recursive solution
def countCoinsRec(coins, length, amount):
	if amount == 0:
		return 1

	if amount < 0:
		return 0

	# amount needed, but no coins left, solution not possible
	if amount >= 1 and length <= 0:
		return 0

	# current coin is either included or excluded
	return countCoins(coins, length-1, amount) + countCoins(coins, length, amount-coins[length-1])

# DP solutions
# time complexity: O(length*amount), space complexity: O(length*amount)
def countCoinsDP(coins, length, amount):
	table = [[0 for i in range(amount + 1)] for j in range(length + 1)]
	
	for row in range(length+1):
		for amt in range(amount+1):
			if amt == 0:
				table[row][amt] = 1
			else:
				if amt >= coins[row-1]:
					table[row][amt] = table[row][amt-coins[row-1]] + table[row-1][amt]
	
	return table[length][amount]

# time complexity: O(length*amount), space complexity: O(amount)
def countCoinsDP2(coins, length, amount):
	table = [0 for i in range(amount+1)]
	table[0] = 1
	
	for row in range(length):
		for amt in range(coins[row], amount+1):
			table[amt] += table[amt-coins[row]]
	
	return table[amount]

coins = [1, 2, 5]
amount = 6
print('Total number of ways is ', end='')
# print(countCoins(coins, len(coins), amount))
# print(countCoinsDP(coins, len(coins), amount))
print(countCoinsDP2(coins, len(coins), amount))
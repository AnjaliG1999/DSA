#!usr/bin/env python3

def editDistance(str1, str2):
	'''
	Memoized bottom-up approach
	Find the minimum number of operations to be performed
	to convert str1 into str2

	:param: str1: string, Initial string
			str2: string, Final string
	:rtype: int
	'''

	table = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]

	for row in range(len(str1)+1):
		for col in range(len(str2)+1):
			
			if row == 0:
				table[row][0] = row

			if col == 0:
				table[0][col] = col

			# no operation needed for the same characters
			if str1[row-1] == str2[col-1]:
				table[row][col] = table[row-1][col-1]
			
			else:
				table[row][col] = 1 + min(
										table[row-1][col-1],	# replace
										table[row][col-1],		# remove
										table[row-1][col]		# insert
										)
	return table[row][col]

def editDistanceRec(str1, str2, len1, len2):
	'''
	Recursive top-down approach
	'''

	if len1 == 0:
		return len2

	if len2 == 0:
		return len1

	if str1[len1-1] == str2[len2-1]:
		return editDistanceRec(str1, str2, len1-1, len2-1)

	return 1 + min(
				editDistanceRec(str1, str2, len1-1, len2-1),	# replace
				editDistanceRec(str1, str2, len1, len2-1),		# remove
				editDistanceRec(str1, str2, len1-1, len2)		# insert
				)

str1 = 'Thursdays'
str2 = 'Sunday'
# print('Minimum editDistance to convert {} into {} is {}'.format(str1, str2, editDistance(str1, str2)))
print('Minimum editDistance to convert {} into {} is {}'.format(str1, str2, editDistanceRec(str1, str2, len(str1), len(str2))))
print('-----Rectangles-----')
# l, b = map(int, input('Enter length and breadth of the rectangle: ').split())
l = 4
b = 7
print(f'Length: {l}, Breadth: {b}')
for _ in range(l):
	print('* '*b)
print()

for i in range(l):
	for j in range(b):
		if i==0 or j==0 or i==l-1 or j==b-1:
			print(end='* ')
		else:
			print(end='  ')
	print()

print()
print('-----Pyramids using stars-----')
level = 5
print(f'Length: {level}')

for i in range(level+1):
	for j in range(i):
		print(end='* ')
	print()

print()
for i in range(level, 0, -1):
	for j in range(i):
		print(end='* ')
	print()

print()
for i in range(level):
	for j in range(level):
		if j>=level-i-1:
			print(end='* ')
		else:
			print(end='  ')
	print()

print()
for i in range(level):
	for j in range(level):
		if j<i:
			print(end='  ')
		else:
			print(end='* ')
	print()

print()
for i in range(level, -1, -1):
	for j in range(i):
		if i==0 or j==0 or i==level or j==i-1:
			print(end='* ')
		else:
			print(end='  ')
	print()

for row in range(1, level):
	k=1 
	for spaces in range(level-row-1):
		print(end='  ')
	for col in range(2*row-1):
		if k:
			print(end='* ')
			k=0
		else:
			print(end='  ')
			k=1

	print()

print()
for row in range(1, level):
	k=1
	for spaces in range(row-1):
		print(end='  ')

	col = 0
	while row+col < 2*level-row-1:
		if k:
			print(end='* ')
			k=0
		else:
			print(end='  ')
			k=1
		col += 1
	print()
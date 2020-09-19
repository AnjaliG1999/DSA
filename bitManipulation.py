# Check if the given integer is even or odd
num1 = 25
print(f'{num1} is odd') if num1 & 1 else print(f'{num1} is even')
print('----------------------------------')

# Detect if 2 integers have the same signs or not 
num2 = -32
print(f'{num1} and {num2} have different signs') if num1^num2 < 0 else print(f'{num1} and {num2} have same signs')
print('----------------------------------')

# Increment the given integer
print(f'{num2} + 1 = {-~num2}')
print('----------------------------------')

# Swap 2 numbers without a temp variable
def swap(num1, num2):
	if num1[0] != num2[0]:
		print(f'Before swapping, num1: {num1[0]}, num2: {num2[0]}')
		num1[0] = num1[0] ^ num2[0]
		num2[0] = num1[0] ^ num2[0]
		num1[0] = num1[0] ^ num2[0]
		print(f'After swapping, num1: {num1[0]}, num2: {num2[0]}')
	else:
		print(f'After swapping, num1, num2: {num1[0]}')

swap([num1], [num1])
print()
swap([num1], [num2])
print('----------------------------------')

# Turn off the k'th bit of an integer
k = 3
num3 = 20
print(f'Number: {num3}')
print(f'After turning k-th bit off: {num3 & ~(1 << k-1)}')
print('----------------------------------')

# Turn on the k'th bit of an integer
k = 4
print(f'Number: {num3}')
print(f'After turning k-th bit off: {num3 | 1 << k-1}')
print('----------------------------------')

# Check if the k'th bit is set for a number
# k = 3
print(f'Number: {num3}')
print('k-th bit is set') if num3 & 1 << k-1 else print('k-th bit is not set')
print('----------------------------------')

# Toggle the k'th bit
print(f'Number before toggle: {num3}')
val = num3 ^ 1 << k-1
print(f'After first toggle: {val}')
print(f'After second toggle: {val ^ 1 << k-1}')
print('----------------------------------')
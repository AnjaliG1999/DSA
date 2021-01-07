def reverseSlicing(str):
    return str[::-1]

def reverseFunction(str):
    return ''.join(reversed(str))

def reversePointer(str):
    str = list(str)
    left = 0
    right = len(str)-1
    while left < right:
        str[left], str[right] = str[right], str[left]
        left += 1
        right -= 1
    return ''.join(str)

def reverseLoop(str):
    s = ""
    for letter in str:
        s = letter + s
    return s

def reverseRecursive(str):
    if not len(str):
        return str
    return reverseRecursive(str[1:])+str[0]

str = "hello"
# reversed = reverseSlicing(str)
# reversed = reverseFunction(str)
# reversed = reversePointer(str)
# reversed = reverseLoop(str)
revStr = reverseRecursive(str)
print(revStr)
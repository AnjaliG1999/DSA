def isPalindromeRecursive(str, n):
    if n == 1 or n == 0:
        return True
    if str[0] == str[-1]:
        return isPalindromeRecursive(str[1:-1], n-2)
    return False

def isPalindrome(str, n):
    if n == 1:
        return True
    flag = False
    for i in range(n//2):
        if str[i] != str[n-i-1]:
            flag = False
            break
        else:
            flag = True
    return flag

def isPalindrome2(str, n):
    if n == 1:
        return True
    left, right = 0, n-1
    flag = False
    while left < right:
        if str[left] != str[right]:
            flag = False
            break
        else:
            flag = True
            left += 1
            right -= 1
    return flag

def isPalindromeSlicing(str, n):
    return str == str[::-1]

str = "abcba"
n = len(str)
pal = isPalindromeRecursive(str, n)
# pal = isPalindrome(str, n)
# pal = isPalindrome2(str, n)
# pal = isPalindromeSlicing(str, n)
if pal:
    print("{} is a palindrome".format(str))
else:
    print("{} is not a palindrome".format(str))
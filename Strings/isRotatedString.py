def isRotated(str1, str2):
    if str2 in str1+str1:
        return True
    return False

str1 = "ABCD"
str2 = "ACBD"
rotated = isRotated(str1, str2)
if rotated:
    print("{} is a rotated string of {}".format(str2, str1))
else:
    print("{} is not a rotated string of {}".format(str2, str1))
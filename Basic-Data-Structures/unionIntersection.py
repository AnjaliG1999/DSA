def printDict(dict):
    for keys in dict:
        print(keys, end=" ")

def fillDictUnion(arr1, arr2):
    unionDict = {}
    for val in arr1:
        if val not in unionDict:
            unionDict[val] = True
    
    for val in arr2:
        if val not in unionDict:
            unionDict[val] = True

    print("Union: ", end="")
    printDict(unionDict)
    

def fillDictIntersection(arr1, arr2):
    intersectionDict = {}
    for val in arr1:
        if val in arr2:
            intersectionDict[val] = True
    
    print("\nIntersection: ", end="")
    printDict(intersectionDict)

def union(arr1, arr2):
    fillDictUnion(arr1, arr2) if len(arr1) > len(arr2) else fillDictUnion(arr2, arr1)
        
def intersection(arr1, arr2):
    fillDictIntersection(arr1, arr2) if len(arr1) < len(arr2) else fillDictIntersection(arr2, arr1)

arr1 = [1, 5, 3, 0, 2, 1, 9]
arr2 = [4, 2, 5, 7]

print("Array1: {}".format(arr1))
print("Array2: {}".format(arr2))
union(arr1, arr2)
intersection(arr1, arr2)
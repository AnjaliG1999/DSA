#!usr/bin/env python3

def merge_list(list1, list2):
    merged_data=""
    resultant_data = []
    n = len(list2)
    for i in range(n):
        if not list1[i]:
            resultant_data.append(list2[n-i-1])
            continue
        if not list2[n-i-1]:
            resultant_data.append(list1[i])
            continue
        merged_data = str(list1[i]+list2[n-i-1])
        resultant_data.append(merged_data)
    resultant_data = " ".join(resultant_data)
    return resultant_data

list1=['T', 'sk', None, 'bl']
list2=['ue', 'is', 'y', 'he']
merged_data=merge_list(list1,list2)
print(merged_data)

# list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
# list2=['y','tor','e','eps','ay',None,'le','n']
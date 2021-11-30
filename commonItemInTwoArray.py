

def findCommon(list1, list2):
    list_as_set = set(list1)
    intersection = list_as_set.intersection(list2)
    print(list(intersection))









# Driver Code
list1 = [1, 2, 3, 4, 4]
list2 = [1, 3]
findCommon(list1, list2)

#removing duplicate characters from a string.

def removeDuplicate(strr):
    newList = []
    for index in strr :
        if index not in newList:
            newList.append(index)
    a = ''.join(newList)
    return a



# Driver code
strr = "geeksforgeeks"
print(removeDuplicate(strr))
#Calculate the frequency of each word in the given string


def printFrequency(strr):

    #define hashmap
    hashMap ={}
    #split the string
    splitStr = strr.split()

    #loop through the string
    for i in range(0, len(splitStr)):
        if splitStr[i] not in hashMap:
            hashMap[splitStr[i]] = 1
        else:
            hashMap[splitStr[i]] += 1
    for index in hashMap:
        print(index, '_', hashMap[index])



# Driver Code
strr = "Geeks For Geeks"
printFrequency(strr)
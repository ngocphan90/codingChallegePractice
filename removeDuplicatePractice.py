

def removeDuplicate(strr):
    strr_map = []
    for character in strr:
        if character not in strr_map:
            strr_map.append(character)
    for i in range (len(strr_map)):
        print(strr_map[i], end='')










# Driver Code
strr = "Geeks For Geeks"
removeDuplicate(strr)

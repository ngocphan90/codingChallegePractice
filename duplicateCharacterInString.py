

def findDuplicate(strr):
    strr_map = {}
    s = ''.join(strr.split())
    print(s)
    for character in s:
        if character in strr_map:
            strr_map[character] += 1
        else:
            strr_map[character] = 1

    for character in strr_map:
        if strr_map[character] > 1:
            print(character, "-", strr_map[character])


# Driver Code
strr = "Geeks For Geeks"
findDuplicate(strr)

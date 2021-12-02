

def removeMostDuplicate(strr):
    strr_map = {}
    max = 0
    s = ''.join(strr.split())

    for character in s:
        if character in strr_map:
            strr_map[character] += 1
        else:
            strr_map[character] = 1

    for character in strr_map:
        if strr_map[character] > max:
            max = strr_map[character]
            maxChar = character

    return strr.replace(maxChar,'')


# Driver Code
strr = "Geeks For Geeks"
print(removeMostDuplicate(strr))

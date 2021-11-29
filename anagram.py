def areAnagram(str1, str2):
    if len(str1) != len(str2):
        return False

    string1 = sorted(str1)
    string2 = sorted(str2)

    for index in range (0, len(string1)):
        if string1[index] != string2[index]:
            return False
    return True








# Driver code
str1 = "ca"
str2 = "act"
# Function Call
if areAnagram(str1, str2):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")
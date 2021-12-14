def areAnagram(str1, str2):
    if len(str1) != len(str2):
        return False

    string1 = sorted(str1)
    string2 = sorted(str2)

    for index in range(0, len(string1)):
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



# check if 2 strings are anagram
#anagram if have the same character but order can be different

def areAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    st1= sorted(str1)
    st2 = sorted(str2)

    for i in range(0, len(st1)):
        if st1[i] != st2[i]:
            return False
    return True





# Driver code
str1 = "cat"
str2 = "act"
# Function Call
if areAnagram(str1, str2):
    print("The two strings are anagram of each other")
else:
    print("Thetwo strings are not anagram of each other")
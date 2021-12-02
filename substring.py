# Python3 program to check if
# a string is substring of other.

# Returns true if s1 is substring of s2
# An efficient solution would need only one traversal i.e.
# O(n) on the longer string s1. Here we will start traversing the string s1 and maintain a pointer for string s2 from 0th index.
# For each iteration we compare the current character in s1 and check it
# with the pointer at s2.
# If they match we increment the pointer on s2 by 1. And for every mismatch we set the pointer back to 0.
# Also keep a check when the s2 pointer value is equal to the length of string s2, if true we break and return the value (pointer of string s1 – pointer of string s2)
def Substr(Str, target):
    t = 0
    Len = len(Str)
    i = 0

    # Iterate from 0 to Len - 1
    for i in range(Len):
        if (t == len(target)):
            break
        if (Str[i] == target[t]):
            t += 1
        else:
            t = 0

    if (t < len(target)):
        return -1
    else:
        return (i - t)


# Driver code
print(Substr("GeeksForGeeks", "For"))


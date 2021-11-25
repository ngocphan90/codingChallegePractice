# Python program to remove duplicate character
# from character array and print in sorted
# order
def removeDuplicate(str, n):
    s = set()

    # Create a set using String characters
    for i in str:
        s.add(i)

    # Print content of the set
    st = ""
    for i in s:
        st = st + i
    return st


# Driver code
str = "geeksforgeeks"
n = len(str)
print(removeDuplicate(list(str), n))
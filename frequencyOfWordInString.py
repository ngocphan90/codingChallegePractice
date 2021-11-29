# Python3 program to calculate the frequency
# of each word in the given string

# Function to print frequency of each word
def printFrequency(strr):
    M = {}

    # string for storing the words
    word = ""

    for i in range(len(strr)):

        # Check if current character
        # is blank space then it
        # means we have got one word
        if (strr[i] == ' '):

            # If the current word
            # is not found then insert
            # current word with frequency 1
            if (word not in M):
                M[word] = 1
                word = ""

            # update the frequency
            else:
                M[word] += 1
                word = ""

        else:
            word += strr[i]

    # Storing the last word of the string
    if (word not in M):
        M[word] = 1

    # Update the frequency
    else:
        M[word] += 1

    # Traverse the map
    # to print the frequency
    for it in M:
        print(it, "-", M[it])


# Driver Code
strr = "Geeks For Geeks"
printFrequency(strr)

# This code is contributed by shubhamsingh10


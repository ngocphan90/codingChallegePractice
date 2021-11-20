# Python code to check if
# a number is jumbled or not

# Function to check if a
# number is jumbled or not
def checkJumbled(num):
    # Single digit number
    if (num / 10 == 0):
        return True

    # Checking every digit
    # through a loop
    while (num != 0):

        # All digits were checked
        if (num / 10 == 0):
            return True

        # Digit at index i
        digit1 = num % 10

        # Digit at index i-1
        digit2 = (num / 10) % 10

        # If difference is
        # greater than 1
        if (abs(digit2 - digit1) > 1):
            return False

        num = num / 10

    # Number checked
    return True


# Driver code

# -1234 to be checked
num = -1234
if (checkJumbled(abs(num))):
    print("True ")
else:
    print("False")

# -1247 to be checked
num = -1247
if (checkJumbled(abs(num))):
    print("True ")
else:
    print("False")


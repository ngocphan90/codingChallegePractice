
def recursiveFactorial(number):

    if number == 2:
        return number
    else:
        return number * recursiveFactorial(number-1)


print(recursiveFactorial(0))
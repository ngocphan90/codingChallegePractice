
def recursiveFactorial(number):
    if number < 2 or number == 2:
        return number
    return number * recursiveFactorial(number-1)


print(recursiveFactorial(4))

def recursiveFactorial(number):
    # if number is 1 or 0 ---return 1
    if number == 2:
        return number
    else:
        return number * recursiveFactorial(number-1)


print(recursiveFactorial(0))
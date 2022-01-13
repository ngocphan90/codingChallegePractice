
def recursiveFactorial(number):
    # if number is 1 or 0 ---return 1
    if number == 1 or number == 0:
        # or if number < 2:
        return number
    else:
        return recursiveFactorial(number-1) + recursiveFactorial(number-2)


print(recursiveFactorial(8))
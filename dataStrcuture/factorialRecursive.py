def recursiveFactorial(number):

    if number == 2:
        return number
    else:
        return number * recursiveFactorial(number-1)


print(recursiveFactorial(0))


# time complexity of this func is O (n):
# calling number of times as the number itself.
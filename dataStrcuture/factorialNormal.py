# 5! = 5X4X3X2X1
# 2 approaches : interative or recursive

 # def iterative(number):

    # array = [0, 1]
    # for i in range (0, n+1):
        # array.push(array[i-2] + array[i-1])
    # return arr[n]

    #  return array[number]



# Python program to find the factorial of a number using recursion


def iterative(number):
    array = [0, 1]
    for i in range(2, number + 1):
        array.append(array[i - 2] + array[i - 1])
    print(number)
    print(array)
    print(array[number])
    return array[number]


print(iterative(2))
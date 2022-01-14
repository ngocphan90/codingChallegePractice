# 5! = 5X4X3X2X1
# 2 approaches : interative or recursive

 # def iterative(number):

    # answer = 1
    # if number == 2:
        # answer = 2
    # for i in range (2, n+1):
        # answer = answer * i


    #  return answer



# time coplexity: O(n)


def iterative(number):
    array = [0, 1]
    for i in range(2, number + 1):
        array.append(array[i - 2] + array[i - 1])
    print(number)
    print(array)
    print(array[number])
    return array[number]


print(iterative(2))
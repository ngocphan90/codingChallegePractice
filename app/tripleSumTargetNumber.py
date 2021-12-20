# Given an array and a value,
# find if there is a triplet in array whose sum is equal to the given value

def tripletDifferentSum(numbers, sum):
    # first approach is 3 nested loop : O(n^3)
    # second approach is 2 pointers: O (n^2)
    # 3rd approach use hash map(using extra space)
    sortedNumber = sorted(numbers)
    print(sortedNumber)
    for i in range(0, len(numbers)):
        l = i + 1
        r = len(numbers) - 1
        while l < r:
            if sortedNumber[i] + sortedNumber[l] + sortedNumber[r] == sum:
                return '3 different number has total sum equal to target: ', \
                       sortedNumber[i] , sortedNumber[l] , sortedNumber[r]
            elif sortedNumber[i] + sortedNumber[l] + sortedNumber[r] < sum:
                l += 1
            else:
                r -= 1
    return False
    # output is 12,3,9


print(tripletDifferentSum([-1, 2, 1, -4], 1))

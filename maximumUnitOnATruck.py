#1710. Maximum Units on a Truck but with 2 separate list

def getMaxUnits(boxes, unitsPerBox, truckSize):
    # create a list of list
    newList = list(zip(boxes, unitsPerBox))
    # sort the new list
    newList.sort(key=lambda x: x[1], reverse=True)
    print(newList)
    maxUnit = 0

    # loop through new list
    for i in newList:
        if truckSize < i[0]:
            return maxUnit + truckSize * i[1]

        maxUnit += i[0] * i[1]
        truckSize -= i[0]

    return maxUnit


if __name__ == '__main__':
    print(getMaxUnits([5, 2, 4, 3],
                      [10, 5, 7, 9], 10))

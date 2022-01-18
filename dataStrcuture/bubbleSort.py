def bubbleSort(array):
    # look at first 2 element and move to the 2nd
    # and 3rd to see which one larger then switch it till the highest number will be at the end
    for i in range(0, len(array)):
        for j in range(0, len(array)-1):
            if array[j] > array[j+1]:
                #swap number
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

print(bubbleSort([2,65,34,1,8]))
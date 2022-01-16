def bubbleSort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array)-1):
            if array[j] > array[j+1]:
                #swap number
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

print(bubbleSort([2,65,34,1,8]))
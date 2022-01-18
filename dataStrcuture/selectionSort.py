# scanning to find the smallest item in
# the list  and at the end switch it with the first item
def selectionSort(array):
    for i in range(0, len(array)):
        min = i
        temp = array[i]
        for j in range(i+1, len(array)):

            if array[j] < array[min]:
                min = j

        array[i] = array[min]
        array[min] = temp
    return array




print(selectionSort([2,65,34,1,8]))
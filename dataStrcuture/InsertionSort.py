#assume 1st card is sorted.
#Take the second element and stored it as a key.
#compare the key with each element on the left until an element smaller than it is found .

def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertionSort([2,65,34,1,8]))
def printRepeating(arr, size):
    print("The repeating elements are: ")

    for i in range(0, size):

        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")



def get_dups(array):
    ht = {}
    dups = []
    for x in array:
        if x in ht:
            dups.append(x)
        else:
            ht[x] = x
    return list(set(dups))

print (get_dups( [1,2,1,3,6,5]))


# Driver code
arr = [1, 2, 3, 1, 3, 6, 6]
arr_size = len(arr)

printRepeating(arr, arr_size)
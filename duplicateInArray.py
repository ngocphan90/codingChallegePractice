# each integer appears once or twice, return an array of all the integers that appears twice.
def printDuplicates(arr):
    arr.sort()
    ans = []
    print(arr)

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:

            ans.append(arr[i])
            i += 1
    return ans






# Driver Code
if __name__ == "__main__":
    list = [12, 11, 40, 12, 5, 6, 5, 11]
    print(printDuplicates(list))
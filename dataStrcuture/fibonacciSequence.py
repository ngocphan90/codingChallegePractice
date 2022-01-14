# // 0,1,1,2,3,5,8,13,21,24
# given a number the func to receive return the index value of fibonacci sequence


def iterative(n):
    arr = [0, 1]
    for i in range(2, n + 1):
        arr.append(arr[i-2] + arr[i-1])
    return arr[n]
# big O is O(n)


print(iterative(4))


def fibonacciRecurisve (n):
    if n < 2:
        return n
    else:
        return fibonacciRecurisve(n-1) + fibonacciRecurisve(n-2)
# big O is O(2^n) : recursive function THAT SOLVES A PROBLEM OF SIZE N
#print(fibonacciRecurisve(0))
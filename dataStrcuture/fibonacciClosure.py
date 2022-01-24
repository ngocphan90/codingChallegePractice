cache = {0: 0, 0: 1}


def fibonacciMaster(n, cache):
    if n in cache:
        return cache[n]

    else:
        cache[n] = fibonacciMaster(n - 1, cache) + fibonacciMaster(n - 2, cache)
        return cache[n]


print(fibonacciMaster(4, cache))

# or using for loop <= nappend to list =[0,1] return answer.pop() # last item in the array



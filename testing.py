def fib(n):
    memo = [-1]*20
    if n <= 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(4))
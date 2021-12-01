# Function for nth Fibonacci number

def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)








# Driver Program

print(Fibonacci(3))
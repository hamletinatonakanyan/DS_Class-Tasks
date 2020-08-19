# 1.Write a Python function which returns factorial value of given number n.

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)


# 2. Write a Python function which returns the n-th element of the fibonacci series.

def fibonacci(n_th):
    if n_th == 0:
        return 0
    if n_th == 1:
        return 1
    return fibonacci(n_th - 1) + fibonacci(n_th-2)


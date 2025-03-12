def fib(n):
    x, y = 0, 1
    for _ in range(n):
        print(x, end=" ")
        x, y = y, x + y

fib(10)

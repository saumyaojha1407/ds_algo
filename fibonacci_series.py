def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    # print(fib(1))
    # print(fib(2))
    # print(fib(6))
    # print(fib(7))
    print(fib(50))
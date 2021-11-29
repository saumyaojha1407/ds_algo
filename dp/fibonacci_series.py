'''
memoization
keys - arg to fib and value will be return value
'''


def fib(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

if __name__ == '__main__':
    # print(fib(1))
    # print(fib(2))
    # print(fib(6))
    # print(fib(7))
    print(fib(100, {}))
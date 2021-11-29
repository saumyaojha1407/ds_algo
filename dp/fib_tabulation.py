def fib_tab(n, list_fib):
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2, n+1):
        list_fib[i] = list_fib[i-1] + list_fib[i-2]
    return list_fib[n]


if __name__ == '__main__':
    print(fib_tab(100,[0, 1] + [0]*99))
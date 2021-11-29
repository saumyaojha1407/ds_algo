

def gridTraveller(n,m, memo):
    if m==1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    if (m,n) in memo:
        return memo[(m,n)]
    if (n,m) in memo:
        return memo[(n,m)]
    memo[(n,m)] = gridTraveller(n-1, m, memo) + gridTraveller(n, m-1, memo)
    return memo[(n,m)]


if __name__ == '__main__':
    # print(fib(1))
    # print(fib(2))
    # print(fib(6))
    # print(fib(7))
    print(gridTraveller(18,18, {}))
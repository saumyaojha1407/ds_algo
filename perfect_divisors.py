def Solve(N):
    # Write your code here
    number = N
    count = 0
    start = N
    while start >= 1:
        if number % start == 0 and start != N:
            count = count + start
        print(count)
        start -= 1
    if count == N:
        return "YES"
    return "NO"


if __name__ == '__main__':
   print(Solve(6))
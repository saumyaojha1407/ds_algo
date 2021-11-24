def findMinDays(n, m):
    if n == m:
        return 0
    if n > m:
        return n - m
    if n <= 0 and m > 0:
        return -1
    if m % 2 == 1:
        return 1 + findMinDays(n, m + 1)
    else:
        return 1 + findMinDays(n, m / 2)


# Driver code
n = 10
m = 1

print(findMinDays(n, m))
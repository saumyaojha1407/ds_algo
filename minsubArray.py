'''
minimum length of subarray in which the sum is greater than k
'''


def minSubArray():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 20
    start = 0
    sum_var = 0
    ans = len(arr)

    for i in range(0, len(arr)):
        sum_var += arr[i]
        if sum_var > k:
            while (start <= i and sum_var - arr[start] > k):
                start += 1
                sum_var -= arr[start]
            ans = min(ans, i - start + 1)
    print(ans)


minSubArray()
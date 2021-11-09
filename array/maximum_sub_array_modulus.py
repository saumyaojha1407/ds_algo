from bisect import bisect, insort

##brute_force
def max_sub_array_brute(arr, mod):
    max_mod = 0
    for i, value in enumerate(arr):
        sum = 0
        for j in range(i, len(arr)):
            sum = sum + arr[j]
            if sum%mod > max_mod:
                max_mod = sum%mod

    return max_mod

def max_sub_array(arr, mod):
    sum = 0
    max_mod = 0
    start = 0
    for i, value in enumerate(arr):
        sum = 0
        for j in range(i, len(arr)):
            sum = sum + arr[j]
            if sum%mod > max_mod:
                max_mod = sum%mod

    return max_mod

def max_sub(ar, M):
    # T = int(input())
    # for _ in range(T):
    #     N, M = [int(i) for i in input().split()]
    #     ar = [int(i) for i in input().split()]

    cumulative_sums = []
    sum_so_far = 0
    max_sum = 0
    for i in range(len(ar)):
        sum_so_far = (sum_so_far + ar[i]) % M
        pos = bisect(cumulative_sums, sum_so_far)
        d = 0 if pos == i else cumulative_sums[pos]
        max_sum = max(max_sum, (sum_so_far + M - d) % M)
        insort(cumulative_sums, sum_so_far)

    return max_sum

print(max_sub([1,2,3], 2))
print(max_sub([3,3,9,9,5], 7))
print(max_sub([1,5,9], 5))
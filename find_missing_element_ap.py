"""
Find the missing number in Arithmetic Progression

Given an array that represents elements of arithmetic progression in order. One element is missing in the progression, find the missing number.

"""

def find(arr):
    d1 = arr[1] - arr[0]
    d2 = arr[2] - arr[1]
    if abs(d2) < abs(d1):
        d = d2
    else:
        d = d1
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != d:
            return arr[i-1] + d

    return -1

def binary_find(arr):
    d1 = arr[1] - arr[0]
    d2 = arr[2] - arr[1]
    if abs(d2) < abs(d1):
        d = d2
    else:
        d = d1
    l = 0
    r = len(arr) -1
    while(l<=r):
        mid = (l + r)//2
        if arr[mid+1] - arr[mid] == d:
            if mid >= r - mid+1:
                l = mid
            else:
                r = mid
        else:
            return arr[mid] + d

test_case = [[5,7,11,13], [12,14, 15],[2, 4, 8, 10, 12, 14], [1, 6, 11, 16, 21, 31], [15, 13, 12]]

for case in test_case:
    print(binary_find(case))



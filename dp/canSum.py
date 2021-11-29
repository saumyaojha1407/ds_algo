def canSumBrute(target, arr):
    if target == 0:
        return True
    if target < 0:
        return False
    for i in arr:
        remainder = target - i
        if canSumBrute(remainder, arr):
            return True
    return False


def canSum(target, arr, memo):
    if target in memo:
        return memo[target]
    if target == 0 and not memo:
        return False
    if target == 0 and memo:
        return True
    if target < 0:
        return False
    for i in arr:
        remainder = target - i
        if canSum(remainder, arr, memo):
            memo[remainder] = True
            return True
    memo[target] = False
    return False




if __name__ == '__main__':
    print(canSum(7, [5,4,3,7], {}))
    print(canSum(7, [2,3], {}))
    print(canSum(7, [2,4], {}))
    print(canSum(8, [2,3,5], {}))
    print(canSum(300, [7,14], {}))
    print(canSum(0, [7, 14], {}))
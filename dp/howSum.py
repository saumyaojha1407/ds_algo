def howSumBrute(target, arr):
    if target == 0:
        return []
    if target < 0:
        return None
    for i in arr:
        remainder = target - i
        remainder_result = howSumBrute(remainder, arr)
        if remainder_result is not None:
            return [] + remainder_result + [i]
    return None


def howSum(target, arr, memo):
    if target in memo:
        return memo[target]
    if target == 0 and not memo:
        return None
    if target == 0 and memo:
        return []
    if target < 0:
        return None
    for i in arr:
        remainder = target - i
        remainder_result = howSum(remainder, arr, memo)
        if remainder_result is not None:
            memo[target] =[] + remainder_result + [i]
            return memo[target]
    memo[target] = None
    return None


def shortesthowSum(target, arr, memo):
    if target in memo:
        return memo[target]
    if target == 0 and not memo:
        return None
    if target == 0 and memo:
        return []
    if target < 0:
        return None
    for i in arr:
        remainder = target - i
        remainder_result = howSum(remainder, arr, memo)
        if remainder_result is not None:
            memo[target] =[] + remainder_result + [i]
            return memo[target]
    memo[target] = None
    return None


# def get_shortest(target, arr, memo):
#     shortest_len = 0
#     output = []
#     memo = get_shortest(target, arr, memo)
#     for key, value in memo.items():
#         if key == target and value:
#             if len(value) > shortest_len:
#                 shortest_len = len(value)
#                 output = value
#     return output


if __name__ == '__main__':
    print(howSum(7, [5,4,3,7], {}))
    print(howSum(7, [2,3], {}))
    print(howSum(7, [2,4], {}))
    print(howSum(8, [2,3,5], {}))
    print(howSum(300, [7,14], {}))
    print(howSum(0, [7, 14], {}))
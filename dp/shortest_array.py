def shortestBrute(target, arr):
    if target == 0:
        return []
    if target < 0:
        return None
    shortest_combination = None
    for i in arr:
        remainder = target - i
        remainder_result = shortestBrute(remainder, arr)
        if remainder_result is not None:
            regular_combination = [] + remainder_result + [i]
            if not shortest_combination or len(shortest_combination) > len(regular_combination):
                shortest_combination = regular_combination

    return shortest_combination


def shortest(target, arr, memo):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    shortest_combination = None
    for i in arr:
        remainder = target - i
        remainder_result = shortest(remainder, arr, memo)
        if remainder_result is not None:
            regular_combination = [] + remainder_result + [i]
            if not shortest_combination or len(shortest_combination) > len(regular_combination):
                shortest_combination = regular_combination
                # memo[remainder] = shortest_combination

    memo[target] = shortest_combination
    return shortest_combination




if __name__ == '__main__':
    print(shortest(7, [5,4,3,7], {}))
    print(shortest(7, [2,3], {}))
    print(shortest(7, [2,4], {}))
    print(shortest(8, [2,3,5], {}))
    print(shortest(300, [7,14], {}))
    print(shortest(0, [7, 14], {}))
    print(shortest(100, [1,2,5,25], {}))
    # print(shortestBrute(7, [5, 4, 3, 7]))
    # print(shortestBrute(7, [2, 3]))
    # print(shortestBrute(7, [2, 4]))
    # print(shortestBrute(8, [2, 3, 5]))
    # print(shortestBrute(300, [7, 14]))
    # print(shortestBrute(0, [7, 14]))
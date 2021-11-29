def get_tab(n, nums):
    list_start = [False] *(n+1)
    list_start[0] = True
    for i in range(0, n+1):
        if list_start[i]:
             for j in nums:
                if j+i >n:
                    continue
                else:
                    list_start[j+i] = True

    return list_start


def canSumTab(n, nums, list_tab):
    return list_tab[n]


if __name__ == '__main__':
    list_tab = get_tab(7, [5,4,3,7])
    print(canSumTab(7, [5,4,3,7], list_tab))
    list_tab = get_tab(7, [2,3])
    print(canSumTab(7, [2,3], list_tab))
    list_tab = get_tab(7, [2,4])
    print(canSumTab(7, [2,4], list_tab))
    list_tab = get_tab(8, [2,3,5])
    print(canSumTab(8, [2,3,5], list_tab))
    list_tab = get_tab(300, [7,14])
    print(canSumTab(300, [7,14], list_tab))
    list_tab = get_tab(0, [7, 14])
    print(canSumTab(0, [7, 14], list_tab))
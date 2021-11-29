def shortestArrayTab(n, nums):
    list_tab = [None] * (n+1)
    list_tab[0] = []
    for i in range(0, n+1):
        if list_tab[i] is not None:
            for j in nums:
                if j+i < n+1:
                    if list_tab[j+i] and len(list_tab[j+i]) < len(list_tab[i]+[j]) :
                        continue
                    list_tab[j+i] = list_tab[i] + [j]
    return(list_tab[n])

if __name__ == '__main__':
    print(shortestArrayTab(7, [5, 4, 3, 7]))
    print(shortestArrayTab(7, [2, 3]))
    print(shortestArrayTab(7, [2, 4]))
    print(shortestArrayTab(8, [2, 3, 5]))
    print(shortestArrayTab(300, [7, 14]))
    print(shortestArrayTab(0, [7, 14]))

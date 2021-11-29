def gridTravellTab(m,n,tab):
    for i in range(1, m+1):
        for j in range(1,n+1):
            tab[i][j] = tab[i-1][j] + tab[i][j-1]
    return tab[m][n]


if __name__ == '__main__':
    list_start = [[0]*10]*10
    list_start[1][1] = 1
    print(gridTravellTab(0,0,list_start))
def find_path(maximum,forward, backward):
    combined = [[i, j] for i in forward for j in backward]
    lessThanMax = []
    for i in range(len(combined)):
        if combined[i][0][1] + combined[i][1][1] <= maximum:
            lessThanMax.append([combined[i][0],combined[i][1]])
    largest = max(lessThanMax, key=lambda x:x[0][1] + x[1][1])
    route = [path[0] for path in largest]
    print(route)


if __name__ == '__main__':
    print(find_path(1000, [[1, 3000], [2, 5000], [3, 7000], [1, 40000]], [[1, 2000], [2, 3000], [3, 4000], [1, 5000]]))
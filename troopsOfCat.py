def getMinimumSeconds(heights, h, u, v):
    minimumSeconds = 0
    if (u+u <= v):
        return len(heights) * u
    heights = sorted(heights)
    print(heights)
    i = 0
    j = len(heights) - 1
    while (i <= j):
        if i != j and (heights[j] + heights[i]) < h:
            i+=1
            minimumSeconds += v
        else:
            minimumSeconds += u
        j-=1
    return minimumSeconds


print(getMinimumSeconds([1,2,3], 4, 2, 3))
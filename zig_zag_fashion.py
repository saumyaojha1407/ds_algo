
m=3
n=3
queue = [(0,0)]
count = 0
i=0
j=0
while queue:
    value = queue.pop(0)
    i = value[0]
    j= value[1]
    if i == m-1 and j == n-1:
        count +=1
    if i+1<m:
        queue.append([i+1,j])
    if j+1<n:
        queue.append([i, j+1])

print(count)
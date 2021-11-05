arr = [5,5,10,100,10,5]
k=2
sum_1=0
sum_2=0
j=0
i=1
for _ in range(0,k):
    if j < len(arr):
        sum_1 += arr[j]
    if i < len(arr):
        sum_2 += arr[i]
    j += 2
    i += 2

max = max(sum_1, sum_2)

j=0
i=1
# for _ in range(len(arr)):
#     if sum_1 + arr[]-arr[i]
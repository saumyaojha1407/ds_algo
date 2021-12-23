# Python 3 Program for the above approach

# Function to find the count of integers
# such that A[i]%A[j] = 0 or A[j]%A[i] = 0
# for each index of the array A[]
def countIndex(A, N):
    # Stores the maximum integer in A[]
    MAX = max(A)
    # Stores the frequency of each
    # element in the array A[]
    freq = [0 for i in range(MAX+1)]

    for i in range(N):
        freq[A[i]] += 1

    # Stores the valid integers in A[]
    # for all integers from 1 to MAX
    res = [0 for i in range(MAX+1)]

    for i in range(1, MAX + 1, 1):
        for j in range(i, MAX + 1, i):
            res[j] +=1

    # Loop to print answer for
    # each index of array A[]
    max_degree = 0
    for i in res:
        if i > max_degree:
            max_degree = i
    print(max_degree)

# Driver Code
if __name__ == '__main__':
    A = [2,2,2,2,2]
    N = len(A)

    # Function Call
    countIndex(A, N)

    # This code is contributed by SURENDRA_GANGWAR.
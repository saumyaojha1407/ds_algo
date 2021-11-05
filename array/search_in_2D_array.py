"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # m, n = len(matrix), len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == target:
        #             return True
        # return False
        # start_row = -1
        # for i in range(m):
        #     if matrix[i][n - 1] == target:
        #         return True
        #     if matrix[i][n - 1] > target:
        #         start_row = i
        #         break
        # if start_row == -1:
        #     return False
        # for i in range(n):
        #     if matrix[start_row][i] == target:
        #         return True
        # return False
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m * n - 1

        while start <= end:
            mid = (start + end) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

abc = Solution()

test_case = [[[1,3,5,7],[10,11,16,20],[23,30,34,60]],
             [[1,3,5,7],[10,11,16,20],[23,30,34,60]]]
target = [3, 13]

for idx, case in enumerate(test_case):
    print(abc.searchMatrix(case, target[idx]))
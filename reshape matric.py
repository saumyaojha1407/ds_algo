from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        i, j = r-1, c-1
        m,n  = 0, 0
        if r*c != len(mat[0])*len(mat):
            return mat
        else:
            output_mat = []
            while i >=0:
                temp_mat = []
                j = c-1
                while j>=0:
                    if n>len(mat[0]) - 1:
                        m +=1
                        n =0
                    temp_mat.append(mat[m][n])
                    n +=1
                    j -= 1
                output_mat.append(temp_mat)
                i -= 1
            return output_mat


obj = Solution()
print(obj.matrixReshape(mat = [[1,2],[3,4]], r = 4, c = 1))
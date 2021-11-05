from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            out = [[1], [1,1]]
            for i in range(2, numRows):
                new_row = []
                j = 0
                for j in range(0, i+1):
                    if j==0 or j==i:
                        new_row.append(1)
                    else:
                        new_row.append(out[i-1][j-1] + out[i-1][j])
                out.append(new_row)
            return out



obj = Solution()
print(obj.generate(5))
"""
check if a sudoku is valid or not

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        a, b = 0, 0
        """
        check inner matrices
        """
        directions = [(0, 0), (0, 1), (0, 2),
                      (1, 0), (1, 1), (1, 2),
                      (2, 0), (2, 1), (2, 2)]
        for i in range(0, 9):
            if a>=9 or b>=9:
                break
            set_check = set()
            for j in directions:
                if board[a + j[0]][b + j[1]] != ".":
                    if board[a + j[0]][b + j[1]] in set_check:
                        return False
                    set_check.add(board[a + j[0]][b + j[1]])
            a+=3
            if a>=9:
                a = 0
                b+=3

        """
        check rows and columns
        """
        for i in range(0, 9):
            set_check = set()
            set_check_2 = set()
            for j in range(0, 9):
                if board[i][j] != ".":
                    if board[i][j] in set_check:
                        return False
                    set_check.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in set_check_2:
                        return False
                    set_check_2.add(board[j][i])
        return True


abc = Solution()
test_cases = [[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]],

[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]],

              [[".", ".", ".", ".", "5", ".", ".", "1", "."],
               [".", "4", ".", "3", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", "3", ".", ".", "1"],
               ["8", ".", ".", ".", ".", ".", ".", "2", "."],
               [".", ".", "2", ".", "7", ".", ".", ".", "."],
               [".", "1", "5", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", "2", ".", ".", "."],
               [".", "2", ".", "9", ".", ".", ".", ".", "."],
               [".", ".", "4", ".", ".", ".", ".", ".", "."]]
              ]
for board in test_cases:
    print(abc.isValidSudoku(board))
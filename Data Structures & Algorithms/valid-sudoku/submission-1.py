"""
Idea:
1. check all rows
2. check all cols
3. check all 9 grids


T: O(N*N)
S: O(N*N)
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def validate_row(row):
            seen = set()
            for j in range(9):
                if board[row][j] in seen and board[row][j] != ".":
                    return False
                seen.add(board[row][j])
            return True

        def validate_col(col):
            seen = set()
            for i in range(9):
                if board[i][col] in seen and board[i][col] != ".":
                     return False
                seen.add(board[i][col])
            return True
        
        def validate_grid(row, col):
            seen = set()
            for i in range(row, row+3):
                for j in range(col, col+3):
                    if board[i][j] in seen and board[i][j] != ".": 
                        return False
                    # print(i, j, board[i][j])
                    seen.add(board[i][j])
            return True


        for row in range(9):
            if not validate_row(row): return False
        
        for col in range(9):
            if not validate_col(col): return False
        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not validate_grid(row, col): return False
        
        return True
        
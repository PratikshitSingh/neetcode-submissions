class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        1. check for first char match - to start search
        2. dont stuck in inf recursion
            -> keep a visited to track
        """
        rows, cols = len(board), len(board[0])

        def word_check(r, c, visited, curr_word):
            if not(0<=r<len(board) and 0<=c<len(board[0]) and not visited[r][c]): return False
            
            visited[r][c] = 1
            if board[r][c] == word[len(curr_word)]:
                curr_word += board[r][c]

                if curr_word == word: return True

                if word_check(r+1, c, visited, curr_word): return True
                if word_check(r-1, c, visited, curr_word): return True
                if word_check(r, c+1, visited, curr_word): return True
                if word_check(r, c-1, visited, curr_word): return True
            visited[r][c] = 0
            return False
            

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    visited = [ [0]*cols for _ in range(rows) ]
                    if word_check(r, c, visited, ""):
                        return True
        return False
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Method-
        0. keep a visited matrix
        1. start dfs at 1 that are not visited yet
        2. at every dfs islands += 1

        T: O(N*M)
        S: O(N*M)
        """
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = [[0]*cols for _ in range(rows)]

        def dfs(r, c):
            if not(0<=r<rows and 0<=c<cols) or (grid[r][c]=="0") or visited[r][c]: return
            visited[r][c] = 1
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and not visited[r][c]:
                    islands += 1
                    dfs(r, c)

        return islands
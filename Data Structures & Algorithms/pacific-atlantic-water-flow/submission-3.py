class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Do reverse BFS from ocean nodes and find nodes present in both BFS
        """
        pac_q, atl_q = deque(), deque()
        rows, cols = len(heights), len(heights[0])

        for i in range(rows):
            pac_q.append((i,0))
            atl_q.append((i,cols-1))

        for j in range(cols):
            pac_q.append((0,j))
            atl_q.append((rows-1,j))

        pacific = set()
        visited = set()
        while pac_q:
            r, c = pac_q.popleft()
            pacific.add((r, c))
            
            if 0<=r+1<rows and heights[r][c]<=heights[r+1][c] and (r+1, c) not in visited:
                visited.add((r+1, c))
                pac_q.append((r+1, c))
            if 0<=r-1<rows and heights[r][c]<=heights[r-1][c] and (r-1, c) not in visited:
                visited.add((r-1, c))
                pac_q.append((r-1, c))
            if 0<=c+1<cols and heights[r][c]<=heights[r][c+1] and (r, c+1) not in visited:
                visited.add((r, c+1))
                pac_q.append((r, c+1))
            if 0<=c-1<cols and heights[r][c]<=heights[r][c-1] and (r, c-1) not in visited:
                visited.add((r, c-1))
                pac_q.append((r, c-1))

        atlantic = set()
        visited = set()
        while atl_q:
            r, c = atl_q.popleft()
            atlantic.add((r, c))
            
            if 0<=r+1<rows and heights[r][c]<=heights[r+1][c] and (r+1, c) not in visited:
                visited.add((r+1, c))
                atl_q.append((r+1, c))
            if 0<=r-1<rows and heights[r][c]<=heights[r-1][c] and (r-1, c) not in visited:
                visited.add((r-1, c))
                atl_q.append((r-1, c))
            if 0<=c+1<cols and heights[r][c]<=heights[r][c+1] and (r, c+1) not in visited:
                visited.add((r, c+1))
                atl_q.append((r, c+1))
            if 0<=c-1<cols and heights[r][c]<=heights[r][c-1] and (r, c-1) not in visited:
                visited.add((r, c-1))
                atl_q.append((r, c-1))

        return list(pacific & atlantic)
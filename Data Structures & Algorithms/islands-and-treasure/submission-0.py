class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        land = 2147483647
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    queue.append((i,j))
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        while queue:
            row,col = queue.popleft()
            for r,c in directions:
                nr = row+r
                nc = col+c
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==land:
                    grid[nr][nc] = grid[row][col]+1
                    queue.append((nr,nc))
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        fresh_orange = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_orange+=1
        if fresh_orange==0:
            return 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        time = 0
        while queue:
            size = len(queue)
            for i in range(size):
                row, col = queue.popleft()
                for r,c in directions:
                    nr = row+r
                    nc = col+c
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        fresh_orange-=1
                        queue.append((nr,nc))
                        grid[nr][nc]=2
            time+=1
            if fresh_orange==0:
                return time
        return -1

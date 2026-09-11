class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        c = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    c+=1
                    self.count_island(directions, i, j, grid)
        return c
    def count_island(self, directions, i, j, grid):
        stack = []
        stack.append((i,j))
        while stack:
            r, c = stack.pop()
            for row, col in directions:
                new_row = row+r
                new_col = col+c
                if 0<=new_row<len(grid) and 0<=new_col<len(grid[0]):
                    if grid[new_row][new_col]=='1':
                        grid[new_row][new_col] = 0
                        stack.append((new_row,new_col))
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    if board[i][j] == 'O':
                        board[i][j] = '#'
                        queue.append((i, j))
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        while queue:
            row,col = queue.popleft()
            for r,c in directions:
                nr = row+r
                nc = col+c
                if 0<=nr<len(board)-1 and 0<=nc<len(board[0])-1:
                    if board[nr][nc]=='O':
                        board[nr][nc]='#'
                        queue.append((nr,nc))
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='#':
                    board[i][j]='O'

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        def dfs(x, y):
            if x < 0 or y < 0 or x == len(board) or y == len(board[0]):
                return
            if board[x][y] == "X":
                return
            if (x,y) in visited:
                return
            if board[x][y] == "O":
                visited.add((x,y))
            
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    if i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1:
                        dfs(i,j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"
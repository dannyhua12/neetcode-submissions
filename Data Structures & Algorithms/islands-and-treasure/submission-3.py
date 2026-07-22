from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        chests = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    chests.append((i,j))
        
        def bfs(pos):
            while pos:
                x,y = pos.popleft()
                if x+1 < len(grid) and grid[x+1][y] == 2147483647:
                    pos.append((x+1,y))
                    grid[x+1][y] = grid[x][y]+1
                if x-1 >= 0 and grid[x-1][y] == 2147483647:
                    pos.append((x-1,y))
                    grid[x-1][y] = grid[x][y]+1
                if y+1 < len(grid[0]) and grid[x][y+1] == 2147483647:
                    pos.append((x,y+1))
                    grid[x][y+1] = grid[x][y]+1
                if y-1 >= 0 and grid[x][y-1] == 2147483647:
                    pos.append((x,y-1))
                    grid[x][y-1] = grid[x][y]+1
        
        bfs(chests)
        
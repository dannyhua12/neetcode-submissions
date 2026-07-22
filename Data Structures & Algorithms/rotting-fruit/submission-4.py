from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                if grid[i][j] == 1:
                    fresh+=1
        count = 0
        def bfs(pos):
            while pos:
                nonlocal count
                nonlocal fresh
                changed = False
                for i in range(len(pos)):
                    x,y = pos.popleft()
                    if x+1 < len(grid) and grid[x+1][y] == 1:
                        grid[x+1][y] = 2
                        pos.append((x+1,y))
                        changed = True
                        fresh-=1
                    if x-1 >= 0 and grid[x-1][y] == 1:
                        grid[x-1][y] = 2
                        pos.append((x-1,y))
                        changed = True
                        fresh-=1
                    if y+1 < len(grid[0]) and grid[x][y+1] == 1:
                        grid[x][y+1] = 2
                        pos.append((x,y+1))
                        changed = True
                        fresh-=1
                    if y-1 >= 0 and grid[x][y-1] == 1:
                        grid[x][y-1] = 2
                        pos.append((x,y-1))
                        changed = True
                        fresh-=1
                if changed:
                    count+=1
        
        bfs(rotten)
        if fresh > 0:
            return -1
        return count
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x,y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return 0
            if grid[x][y] == 0:
                return 0
            
            if grid[x][y] == 1:
                grid[x][y] = 0
            

            return 1 + dfs(x+1, y) + dfs(x-1, y)+ dfs(x, y+1) + dfs(x, y-1)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, dfs(i,j))
        
        return res
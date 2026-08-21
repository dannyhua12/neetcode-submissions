class Solution:
    def climbStairs(self, n: int) -> int:
        tracked = {}

        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            
            
            if i in tracked:
                return tracked[i]

            tracked[i] = dfs(i+1) + dfs(i+2)
            return tracked[i]
        

        return dfs(0)
        


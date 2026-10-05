class Solution:
    def climbStairs(self, n: int) -> int:
        tracked = {}

        def dp(i):
            if i == n:
                return 1
            if i > n:
                return 0
            
            if i in tracked:
                return tracked[i]
            
            tracked[i] = dp(i+1) + dp(i+2)
            return tracked[i]
        return dp(0)
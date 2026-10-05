class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        tracked = {}

        def dp(i):
            if i >= len(cost):
                return 0
            
            if i in tracked:
                return tracked[i]
            
            tracked[i] = cost[i] + min(dp(i+1), dp(i+2))
            return tracked[i]
        
        return min(dp(0), dp(1))
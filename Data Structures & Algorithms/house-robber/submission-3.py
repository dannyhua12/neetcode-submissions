class Solution:
    def rob(self, nums: List[int]) -> int:
        tracked = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in tracked:
                return tracked[i]
            
            tracked[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return tracked[i]
        
        return dfs(0)
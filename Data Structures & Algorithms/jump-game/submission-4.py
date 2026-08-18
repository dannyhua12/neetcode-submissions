class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0 

        for i in range(len(nums)):
            if i > farthest:
                return False
            else:
                farthest = max(i+nums[i], farthest)
        
        return farthest >= len(nums)-1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = 0

        for num in nums:
            curr = max(curr+num, num)
            res = max(curr, res)
        
        return res
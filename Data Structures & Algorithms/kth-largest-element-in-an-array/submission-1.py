import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]

        if len(nums) == 0:
            return 0
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        
        return -nums[0]

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []

        def backtrack(i, subset, total):
            if total == target:
                sol.append(subset[:])
                return
            if total > target:
                return
            if i >= len(nums):
                return
            
            subset.append(nums[i])
            backtrack(i, subset, total+nums[i])
            subset.pop()

            backtrack(i+1, subset, total)
        backtrack(0, [], 0)
        return sol
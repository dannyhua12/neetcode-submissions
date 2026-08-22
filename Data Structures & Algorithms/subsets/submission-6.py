class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []

        def backtracking(subset, i):
            if i == len(nums):
                sol.append(subset[:])
                return
            
            subset.append(nums[i])
            backtracking(subset, i+1)
            subset.pop()

            backtracking(subset, i+1)
        
        backtracking([], 0)
        return sol
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []

        def dfs(i, path):
            if i == len(nums):
                sol.append(path[:])
                return
            
            path.append(nums[i])
            dfs(i+1, path)
            path.pop()

            dfs(i+1, path)
        dfs(0, [])
        return sol
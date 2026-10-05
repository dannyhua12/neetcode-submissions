class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob(arr):
            track = {}

            def dfs(i):
                if i >= len(arr):
                    return 0

                if i in track:
                    return track[i]

                track[i] = max(arr[i] + dfs(i + 2), dfs(i + 1))
                return track[i]
            return dfs(0)
        return max(rob(nums[1:]), rob(nums[:-1]))
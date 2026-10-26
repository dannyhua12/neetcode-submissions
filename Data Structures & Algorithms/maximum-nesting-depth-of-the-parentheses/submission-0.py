class Solution:
    def maxDepth(self, s: str) -> int:
        curr = 0
        maxdepth = 0

        for x in s:
            if x == "(":
                curr+=1
                maxdepth = max(curr, maxdepth)
            elif x == ")":
                curr-=1
        return maxdepth
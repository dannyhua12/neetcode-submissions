class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        tracked = {}
        def dfs(i):
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            
            if i in tracked:
                return tracked[i]

            ways = dfs(i+1)

            if int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26 and i < len(s)-1:
                ways+=dfs(i+2)


            tracked[i] = ways
            return tracked[i]
        return dfs(0)

            
            

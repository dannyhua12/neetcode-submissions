class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        track = set()
        res = 0

        for r in range(len(s)):
            while s[r] in track:
                track.remove(s[l])
                l+=1
            
            track.add(s[r])
            res = max(r-l+1, res)
        
        return res
        
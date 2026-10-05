class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        first = {}

        for s in s1:
            first[s] = first.get(s, 0) +1
        
        second = {}

        l = 0
        for r in range(len(s2)):
            second[s2[r]] = second.get(s2[r],0) +1
            if (r-l+1) > len(s1):
                second[s2[l]]-=1
                if second[s2[l]] == 0:
                    second.pop(s2[l])
                l+=1
            if first == second:
                return True
        return False

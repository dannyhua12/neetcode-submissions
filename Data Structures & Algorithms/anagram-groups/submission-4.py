class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for s in strs:
            sorted_s = "".join(sorted(s))

            if sorted_s not in words:
                words[sorted_s] = []
            
            words[sorted_s].append(s)
        
        return list(words.values())
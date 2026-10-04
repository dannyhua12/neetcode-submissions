class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for word in strs:
            sorted_s = "".join(sorted(word))

            if sorted_s not in words:
                words[sorted_s] = []
            
            words[sorted_s].append(word)
        
        return list(words.values())
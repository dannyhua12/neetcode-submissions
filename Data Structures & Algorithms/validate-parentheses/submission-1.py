class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        

        for cha in s:
            if cha == "(" or cha == "{" or cha == "[":
                stack.append(cha)
            else:
                if not stack or stack.pop() != pairs[cha]:
                    return False
        
        return not stack
                
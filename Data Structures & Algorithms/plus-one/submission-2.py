class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0 
        for digit in digits:
            res*=10
            res+=digit
        res+=1
        n = len(str(res))
        sol = [0]*n

        for i in range(n):
            sol[i] = int(str(res)[i])
        return sol
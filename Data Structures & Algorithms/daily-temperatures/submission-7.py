class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = []

        sol = [0] *len(temperatures)

        for i,t in enumerate(temperatures):
            while temp and t > temp[-1][0]:
                tempt, tempi = temp.pop()
                sol[tempi] = i-tempi
            temp.append([t,i])
        
        return sol
                
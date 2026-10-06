class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        sol = [0] * len(temperatures)

        for i,t in enumerate(temperatures):
            while temps and t > temps[-1][0]:
                tempt, tempi = temps.pop()
                sol[tempi] = i-tempi
            
            temps.append([t, i])
        
        return sol
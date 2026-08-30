class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] *len(temperatures)

        temps = []

        for i, temp in enumerate(temperatures):
            while temps and temp > temps[-1][0]:
                c, index = temps.pop()
                sol[index] = i - index
            temps.append([temp, i])

        return sol
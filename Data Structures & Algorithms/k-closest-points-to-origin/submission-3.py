import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = []

        for i, point in enumerate(points):
            distance = point[0]**2 + point[1]**2
            heapq.heappush(distances, [distance,i])
        
        sol = []
        for i in range(k):
            d, i = heapq.heappop(distances)
            sol.append(points[i])
        
        return sol
            
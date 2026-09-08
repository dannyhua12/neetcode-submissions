import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            temp = heapq.heappop(stones)
            if temp == stones[0]:
                heapq.heappop(stones)
            else:
                difference = temp - stones[0]
                heapq.heappop(stones)
                heapq.heappush(stones, difference)
        if len(stones) == 0:
            return 0
        return -stones[0]

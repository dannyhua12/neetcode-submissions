import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        
        count = {}

        for num in nums:
            count[num] = count.get(num,0)+1
        
        heap = []
        for num, freq in count.items():
            heap.append([-freq,num])
        heapq.heapify(heap)

        for i in range(k):
            freq,num = heapq.heappop(heap)
            res.append(num)
        return res
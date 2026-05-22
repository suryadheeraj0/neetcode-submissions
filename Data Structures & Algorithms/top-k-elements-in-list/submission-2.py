import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        heap = []
        res = []
        for i in d:
            heapq.heappush(heap,(d[i],i))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for count, num in heap]


        

        


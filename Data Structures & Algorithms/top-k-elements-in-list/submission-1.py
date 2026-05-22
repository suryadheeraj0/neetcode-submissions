import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        heap = []
        res = []
        for i in d:
            heapq.heappush(heap,(-d[i],i))
        while k!=0:
            freq, num = heapq.heappop(heap)
            res.append(num)
            k-=1
        return res


        

        


import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dist = math.sqrt(((x-0)**2)+((y-0)**2))
            heapq.heappush(heap, (-dist, [x,y]))
            if len(heap)>k:
                heapq.heappop(heap)
        res = []
        while len(heap)>0:
            x,y = heapq.heappop(heap)
            res.append(y)
        return res
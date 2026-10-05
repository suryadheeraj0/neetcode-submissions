import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        a, b = heap[0]
        res.append(-a)

        for j in range(k, len(nums)):
            heapq.heappush(heap, (-nums[j], j))
            while heap[0][1] <= j - k:
                heapq.heappop(heap)

            a, b = heap[0]
            res.append(-a)

        return res
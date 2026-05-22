from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = []
        for i in range(len(nums)):
            q.append(nums[i])
            if len(q)==k:
                l.append(max(q))
                q.popleft()
        return l

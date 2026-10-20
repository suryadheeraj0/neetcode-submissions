class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        res = float('-inf')
        for i in nums:
            s+=i
            res = max(res, s)
            if s<0:
                s=0
        return res
            
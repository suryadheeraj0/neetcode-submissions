class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        ma = float('-inf')
        for i in nums:
            if s<0:
                s=i
            else:
                s+=i
            ma = max(ma, s)
        return ma
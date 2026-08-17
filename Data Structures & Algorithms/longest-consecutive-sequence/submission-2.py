class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        ma = float('-inf')
        se = set(nums)
        for i in se:
            if (i-1) not in se:
                c = 1
                while i+1 in se:
                    c+=1
                    i+=1
                ma = max(c,ma)
        return ma

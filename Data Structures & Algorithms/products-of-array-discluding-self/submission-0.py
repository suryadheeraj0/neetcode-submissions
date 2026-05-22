class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        d = {}
        curr_ind = 0
        if nums.count(0)>1:
            return [0]*len(nums)
        while curr_ind<len(nums):
            s = 1
            for i in range(len(nums)):
                if i!=curr_ind:
                    s = s*nums[i]
            d[curr_ind] = s
            curr_ind+=1
        res = [0]*len(nums)
        for i in d:
            res[i] = d[i]
        return res

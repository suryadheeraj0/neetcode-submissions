class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = []
        res = []
        def per(l,res,nums):
            if len(l)==len(nums):
                print(l)
                res.append(l[:])
            for i in range(len(nums)):
                if nums[i] not in l:
                    l.append(nums[i])
                    per(l, res, nums)
                    l.pop()
        per(l,res,nums)
        return res
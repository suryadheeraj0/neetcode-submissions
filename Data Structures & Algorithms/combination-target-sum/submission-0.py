class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        l = []
        def comb_sum(nums, res, target, ind):
            if sum(l)>=target:
                if sum(l)==target:
                    if l not in res:
                        res.append(l[:])
                return
            if ind>len(nums)-1:
                return
            l.append(nums[ind])
            comb_sum(nums, res, target, ind)
            l.pop()
            comb_sum(nums, res, target, ind+1)
        comb_sum(nums,res, target, 0)
        return res
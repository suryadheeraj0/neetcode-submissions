class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        def comb(nums, index, target, l):
            if index>=len(nums):
                return
            if sum(l)==target:
                self.res.append(l[:])
                return
            elif sum(l)>target:
                return
            l.append(nums[index])
            comb(nums, index, target, l)
            l.pop()
            comb(nums, index+1, target, l)
        comb(nums, 0, target, [])
        return self.res
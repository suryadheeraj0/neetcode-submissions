class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def per(nums, l):
            if len(l)==len(nums):
                self.res.append(l[:])
                return
            for i in range(len(nums)):
                if nums[i] not in l:
                    l.append(nums[i])
                    per(nums, l)
                    l.pop()
        per(nums, [])
        return self.res
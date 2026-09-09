class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def subset(index, nums, l):
            if index == len(nums):
                self.res.append(l[:])
                return
            l.append(nums[index])
            subset(index+1, nums, l)
            l.pop()
            subset(index+1, nums, l)
        subset(0, nums, [])
        return self.res
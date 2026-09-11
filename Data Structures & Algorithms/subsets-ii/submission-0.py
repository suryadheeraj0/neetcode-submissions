class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        s = set()
        self.res = []
        def subsets(nums, l, index):
            if index == len(nums):
                if tuple(sorted(l)) not in s:
                    self.res.append(l[:])
                s.add(tuple(sorted(l)))
                return
            l.append(nums[index])
            subsets(nums, l, index+1)
            l.pop()
            subsets(nums, l, index+1)
        subsets(nums, [], 0)
        return self.res
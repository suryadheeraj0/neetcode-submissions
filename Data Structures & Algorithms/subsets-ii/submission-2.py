class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        l = []
        res = []
        def subset(l, res, ind):
            if ind>len(nums)-1:
                if sorted(l) not in res:
                    res.append(sorted(l[:]))
                return 
            l.append(nums[ind])
            subset(l, res, ind+1)
            l.pop()
            subset(l, res, ind+1)
        subset(l, res, 0)     
        return res
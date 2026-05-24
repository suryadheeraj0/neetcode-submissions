class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = []
        ans = []
        def subset(nums, l, ans, index):
            if index>len(nums)-1:
                ans.append(l[:])
                return 
            l.append(nums[index])
            subset(nums, l, ans, index+1)
            l.pop()
            subset(nums, l, ans, index+1)
        subset(nums, l, ans, 0)
        return ans
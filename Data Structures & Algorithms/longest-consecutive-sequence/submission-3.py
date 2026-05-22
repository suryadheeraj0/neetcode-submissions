class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=sorted(set(nums))
        ma=0
        c=0
        print(nums)
        for i in range(len(nums)-1):
            if abs(nums[i]-nums[i+1])==1:
                c+=1
                ma=max(ma,c)
            else:
                c=0
        return ma+1
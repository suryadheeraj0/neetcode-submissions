class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=sorted(nums)
        ma=0
        c=0
        print(nums)
        for i in range(len(nums)-1):
            if abs(nums[i]-nums[i+1])==1:
                c+=1
                ma=max(ma,c)
            elif nums[i]==nums[i+1]:
                c+=0
            else:
                c=0
        return ma+1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        se = set()
        res = []
        while i<len(nums)-2:
            j = i+1
            k = len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    if (nums[i],nums[j],nums[k]) not in se:
                        res.append([nums[i],nums[j],nums[k]])
                        se.add((nums[i],nums[j],nums[k]))
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1
            i+=1
        return res

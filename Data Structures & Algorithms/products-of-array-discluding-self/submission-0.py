class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_pro = [0]*len(nums)
        right_pro = [0]*len(nums)
        left_pro[0]=1
        res = [0]*len(nums)
        for i in range(1,len(nums)):
            left_pro[i]=left_pro[i-1]*nums[i-1]
        right_pro[len(nums)-1]=1
        for j in range(len(nums)-1,0,-1):
            right_pro[j-1]=right_pro[j]*nums[j]
        for k in range(len(nums)):
            res[k] = left_pro[k]*right_pro[k]
        return res
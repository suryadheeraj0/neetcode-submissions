class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ma = 0
        for i in range(len(nums)):
            if i>ma:
                return False
            ma = max(ma, nums[i]+i)
            if ma>=len(nums)-1:
                return True
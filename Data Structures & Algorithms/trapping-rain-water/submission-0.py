class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_left = float('-inf')
        max_right = float('-inf')
        s = 0
        while left<right:
            if height[left]<=height[right]:
                max_left = max(max_left,height[left])
                s+=max_left-height[left]
                left+=1
            else:
                max_right = max(max_right,height[right])
                s+=max_right-height[right]
                right-=1
        return s
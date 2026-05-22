class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = len(matrix)-1
        while l<=h:
            mid = (l+h)//2
            if matrix[mid][0]<=target and matrix[mid][-1]>=target:
                return self.check_target(matrix[mid],target)
            elif matrix[mid][0]>target:
                h = mid-1
            else:
                l = mid+1
        return False
    def check_target(self,arr,target):
        print(arr,target)
        l = 0
        h = len(arr)-1
        while l<=h:
            mid = (l+h)//2
            if arr[mid]==target:
                return True
            elif arr[mid]>target:
                h = mid-1
            else:
                l = mid+1
        return False
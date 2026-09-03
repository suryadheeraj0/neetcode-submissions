class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        while left<=right:
            mid = (left+right)//2
            if matrix[mid][0]<=target and matrix[mid][-1]>=target:
                left = 0
                right = len(matrix[mid])-1
                while left<=right:
                    col_mid = (left+right)//2
                    if matrix[mid][col_mid]==target:
                        return True
                    elif matrix[mid][col_mid]>target:
                        right = col_mid-1
                    else:
                        left = col_mid+1
                return False
            elif matrix[mid][0]>target:
                right = mid-1
            else:
                left = mid+1
        return False
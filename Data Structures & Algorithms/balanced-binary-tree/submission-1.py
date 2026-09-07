# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.flag = True
        def isBalance(root):
            if not root:
                return 0
            left = isBalance(root.left)
            right = isBalance(root.right)
            if abs(left-right)>1:
                self.flag = False
            return max(left,right)+1
        isBalance(root)
        return self.flag
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == subRoot.val:
            if self.checkTree(root, subRoot)==True:
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def checkTree(self, root, subRoot):
        if root is None and subRoot is not None:
            return False
        elif root is not None and subRoot is None:
            return False
        elif root is None and subRoot is None:
            return True
        else:
            if root.val!=subRoot.val:
                return False
        return self.checkTree(root.left, subRoot.left) and self.checkTree(root.right, subRoot.right)
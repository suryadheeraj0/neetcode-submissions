class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        self.lca = TreeNode(0)

        def LCA(root: TreeNode, p: TreeNode, q: TreeNode) -> bool:
            if not root:
                return False

            left = LCA(root.left, p, q)
            right = LCA(root.right, p, q)

            if left and right:
                self.lca.val = root.val

            if root.val == p.val and (left or right):
                self.lca.val = root.val

            if root.val == q.val and (left or right):
                self.lca.val = root.val

            if root.val == p.val or (left or right):
                return True

            if root.val == q.val or (left or right):
                return True
            return left or right

        LCA(root, p, q)
        return self.lca
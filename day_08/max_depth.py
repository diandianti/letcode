# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_dep = 0

        def recur(node, dep):
            if node is None:
                return

            self.max_dep = max(dep + 1, self.max_dep)
            recur(node.left, dep + 1)
            recur(node.right, dep + 1)

        recur(root, 0)
        return self.max_dep
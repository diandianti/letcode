# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def recur(node):
            if node is None:
                return

            if self.count > self.k:
                return

            recur(node.left)

            if self.count == self.k:
                self.res = node.val
            self.count += 1

            recur(node.right)

        self.k = k
        self.count = 1
        recur(root)
        return self.res
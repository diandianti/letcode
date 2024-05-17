# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        while node:
            if node.left is None:
                node = node.right
                continue

            pre = node.left
            while pre.right:
                pre = pre.right

            pre.right = node.right
            node.right = node.left
            node.left = None
            node = node.right
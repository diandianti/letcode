# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        def recur(left, right):
            if not (left or right):
                return True

            if not (left and right):
                return False

            if left.val != right.val:
                return False

            return recur(left.left, right.right) and recur(left.right, right.left)

        return recur(root.left, root.right)
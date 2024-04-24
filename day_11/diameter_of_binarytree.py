from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def depth(node):
            if node is None:
                return 0

            dep_l = depth(node.left)
            dep_r = depth(node.right)
            self.ans = max(self.ans, dep_l + dep_r + 1)
            return max(dep_l, dep_r) + 1
        depth(root)
        return self.ans - 1
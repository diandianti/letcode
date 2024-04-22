# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []

        def recur(node):
            if node is None:
                return
            recur(node.left)
            self.res.append(node.val)
            recur(node.right)

        recur(root)
        return self.res
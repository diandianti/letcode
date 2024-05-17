# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.all = []

        def recur(node):
            if node is None:
                return True

            recur(node.left)
            self.all.append(node.val)
            recur(node.right)

        recur(root)

        flag = True
        pre = None
        for i in self.all:
            if (pre is not None) and (i <= pre):
                flag = False
                break
            pre = i

        return flag
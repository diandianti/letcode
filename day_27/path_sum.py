from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def recur(node: Optional[TreeNode], target) -> int:
            if node is None:
                return 0

            res = 0 if node.val != target else 1
            res += recur(node.left, target - node.val)
            res += recur(node.right, target - node.val)
            return res

        if root is None:
            return 0

        ret = recur(root, targetSum)
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)
        return ret

root = TreeNode(10,
                TreeNode(5,
                         TreeNode(3,
                                  TreeNode(3,
                                           TreeNode(3),
                                           TreeNode(-2)),),
                         TreeNode(2, None, TreeNode(-1))),
                TreeNode(-3, TreeNode(11))
                )

print(Solution().pathSum(root, 6))
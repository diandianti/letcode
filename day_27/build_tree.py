from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        l = len(preorder)

        if l == 0:
            return None
        elif l == 1:
            return TreeNode(preorder[0])
        elif l == 2:
            node = TreeNode(preorder[0])
            if preorder[0] == inorder[1]:
                node.left = TreeNode(preorder[1])
            else:
                node.right = TreeNode(preorder[1])
            return node
        # elif l == 3:
        #     node = TreeNode(preorder[0])
        #     node.left = TreeNode(preorder[1])
        #     node.right = TreeNode(preorder[2])
        #     return node

        node = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1: 1 + root_idx], inorder[:root_idx])
        node.right = self.buildTree(preorder[1 + root_idx:], inorder[root_idx + 1:])

        return node

print(Solution().buildTree([1,2,3], inorder = [3,2,1]))


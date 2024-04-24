from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []
        q = [root]

        while q:
            _t = []
            for _ in range(len(q)):
                node = q.pop(0)
                _t.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(_t)
        return res

import copy
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []
        qs = [[root], []]
        cur = False
        tmp = []

        while qs[0] or qs[1]:
            node = qs[cur].pop(0)
            tmp.append(node.val)

            if node.left:
                qs[not cur].append(node.left)

            if node.right:
                qs[not cur].append(node.right)

            if not qs[cur]:
                res.append(copy.copy(tmp))
                tmp.clear()
                cur = not cur

        return res

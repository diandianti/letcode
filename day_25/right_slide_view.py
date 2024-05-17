# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = [[root], []]
        tmp = []
        all = []
        cur = 0
        while queue[0] or queue[1]:
            cur_queue = queue[cur]
            other_queue = queue[not cur]
            node = cur_queue.pop(0)
            tmp.append(node.val)
            if node.left: other_queue.append(node.left)
            if node.right: other_queue.append(node.right)
            if not cur_queue:
                all.append(tmp)
                tmp = []
                cur = not cur

        res = []
        for i in all:
            res.append(i[-1])

        return res

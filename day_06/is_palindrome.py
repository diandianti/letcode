from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        self.pre_node = head

        def recur(cur_node):
            if not (cur_node is None):
                if not recur(cur_node.next):
                    return False

                if cur_node.val != self.pre_node.val:
                    return False

                self.pre_node = self.pre_node.next

            return True

        return recur(head)

class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next

        return vals == vals[::-1]
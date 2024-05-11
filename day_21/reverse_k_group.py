from typing import Optional

from swap_pairs import build_listnodes,show_listnodes
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pre_head = None
        ret = None
        while True:
            node = head
            count = 0
            while k > count and node:
                count += 1
                node = node.next
            if count < k:
                pre_head.next = head
                break

            pre = None
            cur = head
            count = 0
            while k > count:
                count += 1

                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp

            if ret is None:
                ret = pre

            if pre_head:
                pre_head.next = pre

            pre_head = head
            head = cur

        return ret

head = build_listnodes([1,2,3,4,5,6])
res = Solution().reverseKGroup(head, 4)
show_listnodes(res)
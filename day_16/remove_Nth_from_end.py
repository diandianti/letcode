from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        wait_count = 0
        slow_pre = ListNode(next = head)
        head_pre = slow_pre
        slow = head
        fast = head

        while fast:
            if wait_count == n:
                slow_pre, slow = slow, slow.next
            else:
                wait_count += 1
            fast = fast.next

        slow_pre.next = slow.next

        return head_pre.next
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None) or (head.next is None):
            return head

        pre_ret = ListNode()
        pre = pre_ret
        cur1 = head
        cur2 = head.next

        while cur1 and cur2:
            next = cur2.next

            pre.next = cur2
            cur2.next = cur1
            cur1.next = next

            pre = cur1
            cur1 = next

            if cur1 is None:
                break
            else:
                cur2 = next.next

        return pre_ret.next

def build_listnodes(nums:list):
    nums.reverse()
    pre = None
    for i in nums:
        node = ListNode(i, pre)
        pre = node
    return pre

def show_listnodes(head: ListNode):
    node = head
    while node:
        print(f"-> {node.val} ", end="")
        node = node.next
    print()

# head = build_listnodes([1,2,3,4])
# res = Solution().swapPairs(head)
# show_listnodes(res)

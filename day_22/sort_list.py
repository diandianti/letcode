from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        node = head
        tmp = []
        while node:
            tmp.append(node)
            node = node.next

        tmp.sort(key=lambda x: x.val)
        tmp.reverse()

        pre = tmp.pop(0)
        for node in tmp:
            node.next = pre
            pre = node

        return pre
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

head = build_listnodes([1, -1, 3, 2, 5])
res = Solution().sortList(head)
show_listnodes(res)
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _pre = None
        node = head

        while node:
            _next = node.next
            node.next = _pre
            _pre = node
            node = _next

        return _pre

class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recur(pre:ListNode, cur:ListNode):
            if cur.next:
                _next = cur.next
                cur.next = pre
                return recur(cur, _next)
            else:
                cur.next = pre
                return cur

        return recur(None, head) if head else head

def build_list(l:List) -> ListNode:
    _last = None
    _cur = None
    l.reverse()
    for i in l:
        _cur = ListNode(i, _last)
        _last = _cur

    return _cur

if __name__ == "__main__":
    head = build_list([1,2,3,4,5])
    node = head
    while node:
        print(node.val, end="")
        node = node.next
    print()
    node = Solution2().reverseList(head)
    while node:
        print(node.val, end="")
        node = node.next
    print()

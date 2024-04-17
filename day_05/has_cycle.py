class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        _d = {}
        node = head
        while node:
            if node in _d:
                return True
            _d[node] = 1
            node = node.next

        return False


class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next

        return True

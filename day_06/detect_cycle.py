class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _d = {}
        node = head
        while node:
            if node in _d:
                return node
            _d[node] = 1
            node = node.next

        return None

#todo solution2

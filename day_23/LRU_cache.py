from typing import Dict


class ListNode:
    def __init__(self, val:int = 0, key:int = 0, pre:'ListNode' = None, next:'ListNode' = None):
        self.val = val
        self.key = key
        self.pre = pre
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d:Dict[int, ListNode] = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.len = 0

        self.head.next = self.tail
        self.tail.pre = self.head


    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        node = self.d[key]
        node.pre.next = node.next
        node.next.pre = node.pre
        self.tail.pre.next = node
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = value
            node.pre.next = node.next
            node.next.pre = node.pre
        else:
            node = ListNode(value, key)
            self.d[key] = node
            self.len += 1

        self.tail.pre.next = node
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre = node

        if self.len > self.capacity:
            node = self.head.next
            self.head.next = node.next
            node.next.pre = self.head
            self.d.pop(node.key)
            self.len -= 1

obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
val = obj.get(1)
obj.put(3, 3)
val = obj.get(2)
obj.put(4, 4)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
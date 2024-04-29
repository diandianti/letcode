class MinStack:

    def __init__(self):
        self._vals = []
        self._sorts = []


    def push(self, val: int) -> None:
        self._vals.append(val)
        idx = 0
        for v in self._sorts:
            if val >= v:
                break
            idx += 1
        self._sorts.insert(idx, val)

    def pop(self) -> None:
        val = self._vals.pop()
        self._sorts.remove(val)


    def top(self) -> int:
        return self._vals[-1]


    def getMin(self) -> int:
        return self._sorts[-1]



s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)

print(s)
print(s.getMin())
s.pop()
print( s.top())
print( s.getMin())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
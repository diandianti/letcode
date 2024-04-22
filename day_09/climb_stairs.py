class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1: return 1
        if n == 2: return 2
        pp = 1
        p = 2
        for i in range(2, n):
            p, pp = p + pp, p
        return p

class Solution2:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

print(Solution().climbStairs(5))
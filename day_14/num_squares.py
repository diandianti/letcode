import math


class Solution:
    def numSquares(self, n: int) -> int:
        s = {}

        for i in range(1, n + 1):
            if math.sqrt(i).is_integer():
                s[i] = 1
            else:
                j = 1
                j2 = j * j
                _t = i
                while j2 < i:
                    _t = min(s[j2] + s[i - j2], _t)
                    j += 1
                    j2 = j * j
                s[i] = _t

        return s[n]

print(Solution().numSquares(13))


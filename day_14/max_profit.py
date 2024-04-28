from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                m = max(prices[j] - prices[i], m)

        return m

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        m, c = 0, 1e6
        for i in prices:
            c = min(c, i)
            m = max(i - c, m)

        return m

print(Solution2().maxProfit([1,2,11,4,7]))

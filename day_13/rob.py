from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        r = 0
        n = 0
        for i in nums:
            r, n = n + i, max(r,  n)

        return max(r, n)

print(Solution().rob([2,7,9,3,1]))

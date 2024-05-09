from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        ll = len(height)
        if ll < 3:
            return 0

        lmax = [height[0]] + [0] * (ll - 1)
        rmax = [0] * (ll - 1) + [height[ll - 1]]

        for i in range(1, ll):
            lmax[i] = max(lmax[i - 1], height[i])

        for i in range(ll - 2, -1, -1):
            rmax[i] = max((rmax[i + 1], height[i]))

        return sum(min(lmax[i], rmax[i]) - height[i]  for i in range(ll))

print(Solution().trap([4,2,0,3,2,5]))

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        _m = 0
        while l < r:
            _area = (r - l) * min(height[l], height[r])
            _m = max(_area, _m)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return _m

if __name__ == "__main__":
    hs = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(hs))

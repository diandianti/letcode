
import sys
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)

        return max(nums)

class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        m = -1e5
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                m = max(m, sum(nums[i:j]))

        return m

print(Solution().maxSubArray([5,4,-1,7,8]))
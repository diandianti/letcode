from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        _ns = sorted(nums)
        return _ns[-k]


print(Solution().findKthLargest([3,2,1,5,6,4], 2))
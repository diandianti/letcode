import math
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k = k % l

        if k == 0:
            return

        gcd = math.gcd(l, k)
        if gcd == 1:
            idx = 0
            tmp = nums[idx]
            for _ in range(l):
                t_idx = (idx + k) % l
                tmp, nums[t_idx] = nums[t_idx], tmp
                idx = t_idx
        else:
            for i in range(gcd):
                idx = i
                tmp = nums[idx]
                for _ in range(l // gcd):
                    t_idx = (idx + k) % l
                    tmp, nums[t_idx] = nums[t_idx], tmp
                    idx = t_idx

nums = [1,2,3,4,5,6]
Solution().rotate(nums, 3)
print(nums)
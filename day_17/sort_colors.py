from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1s
        cur = 0
        while cur <= r:
            val = nums[cur]
            if val == 0:
                nums[cur], nums[l] = nums[l], nums[cur]
                l += 1
                cur = max(cur, l)
            if val == 2:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1
            if val == 1:
                cur += 1

l = [1,1,1,0,0,2]
Solution().sortColors(l)
print(l)

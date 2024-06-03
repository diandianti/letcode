from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        idx = -1
        for i in range(l - 1, 0, -1): # i in [ l-1, l-2 , ... 3, 2, 1]
            if nums[i - 1] < nums[i]:# !!! must < not <= !!!
                idx = i - 1
                break


        if idx != -1:
            idx_r = l - 1
            while nums[idx_r] <= nums[idx] and idx_r > idx:
                idx_r -= 1

            nums[idx], nums[idx_r] = nums[idx_r], nums[idx]

        nums[idx + 1:] = reversed(nums[idx + 1:])

        return

a = [5,1,1]
Solution().nextPermutation(a)
print(a)

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        left = 0
        right = 0
        while right < l:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        idx = 0
        next_idx = 0
        zero_count = 0
        while idx < l and next_idx < l:
            while next_idx < (l - 1) and nums[next_idx] == 0:
                next_idx += 1
                zero_count += 1

            nums[idx] = nums[next_idx]
            next_idx += 1
            idx += 1

        if zero_count:
            for i in range(1, zero_count + 1):
                nums[-i] = 0

if __name__ == "__main__":
    s = Solution()
    nums = [0,2,3,1,9,0]
    s.moveZeroes(nums)
    print(nums)
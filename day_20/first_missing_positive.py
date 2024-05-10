from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ll = len(nums)
        tmp = [0] * (ll + 1)
        for i in range(ll):
            if nums[i] > ll or nums[i] < 0:
                nums[i] = 0

        for i in nums:
            tmp[i] = 1

        for i in range(1, ll + 1):
            if tmp[i] == 0:
                break

        return i if tmp[i] == 0 else i + 1


class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ll = len(nums)
        for i in range(ll):
            if nums[i] <= 0:
                nums[i] = ll + 1

        for i in range(ll):
            n = abs(nums[i])
            if n <= ll:
                nums[n - 1] = -abs(nums[n - 1])

        for i in range(ll):
            if nums[i] > 0:
                return i + 1

        return ll + 1
print(Solution2().firstMissingPositive([1]))



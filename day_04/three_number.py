from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = []

        for k in range(l - 2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            i = k + 1
            j = l - 1
            _diff = 0 - nums[k]
            while i < j:
                s = nums[i] + nums[j]
                if s == _diff:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while (i < j) and (nums[i] == nums[i - 1]): i += 1
                    while (i < j) and nums[j] == nums[j + 1]: j -= 1

                if s < _diff:
                    i += 1
                    while (i < j) and (nums[i] == nums[i - 1]): i += 1

                if s > _diff:
                    j -= 1
                    while (i < j) and nums[j] == nums[j + 1]: j -= 1

        return res

if __name__ == "__main__":
    print(Solution().threeSum([-2,0,0,2,2]))

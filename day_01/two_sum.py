from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for idx, val in enumerate(nums):
            _idx = temp.get(val, -1)
            if _idx > -1:
                return [_idx, idx]
            diff = target - val
            temp[diff] = idx
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([1,2,3,4,5,7], 8))

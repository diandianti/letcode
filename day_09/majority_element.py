from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        half_len = len(nums) // 2
        for k,v in d.items():
            if v > half_len:
                return k

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for n in nums:
            if votes == 0:
                x = n
            if n == x:
                votes += 1
            else:
                votes -= 1

        return x
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = {}
        for i in nums:
            temp[i] = temp.get(i, 0) + 1

        for k,v in temp.items():
            if v == 1:
                return k

from functools import reduce
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

if __name__ == "__main__":
    s = Solution2()
    print(s.singleNumber([1,2,1,2,3]))
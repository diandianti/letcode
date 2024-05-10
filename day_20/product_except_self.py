from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ll = len(nums)
        res = []
        lp = [1]
        rp = [1] * (ll + 2)

        for i in range(ll):
            lp.append(lp[-1] * nums[i])

        lp.append(1)
        for i in range(ll - 1,  -1, -1):
            rp[i + 1] = nums[i] * rp[i + 2]

        for i in range(1, ll + 1):
            res.append(lp[i - 1] * rp[i + 1])

        return res

class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ll = len(nums)
        res = [1] * ll

        res[0] = nums[0]
        for i in range(1, ll - 1):
            res[i] = res[i - 1] * nums[i]

        tmp = 1
        for i in range(ll - 1, 0, -1):
            res[i] = res[i - 1] * tmp
            tmp *= nums[i]

        res[0] = tmp
        return res

print(Solution2().productExceptSelf([1,2,3,4]))
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        res = []
        q = []
        for i in range(l):
            if not q:
                q.append(i)
            else:
                while q and nums[q[-1]] < nums[i]:
                    q.pop(-1)
                q.append(i)

            if q and q[0] <= (i - k):
                q.pop(0)

            if i >= (k - 1):
                res.append(nums[ q[0] ])

        return res


print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
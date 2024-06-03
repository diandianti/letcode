from typing import List

#https://leetcode.cn/problems/find-the-duplicate-number/description/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return slow

print(Solution().findDuplicate([1, 3, 4, 2, 2]))
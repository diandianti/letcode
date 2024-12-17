#https://leetcode.cn/problems/delete-and-earn/description/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        total = len(nums)
        if total == 1:
            return nums[0]
        if total == 2:
            if abs(nums[0] - nums[1]) == 1:
                return max(nums)
            else:
                return sum(nums)
        nums.sort()

        cur = 0
        dupCount = 1
        preValue = 0

        preTake = 0
        preNoTake = 0
        prePreTake = 0
        prePreNoTake = 0
        
        while cur < total:
            if cur+1 < total and nums[cur] == nums[cur+1]:
                cur += 1
                dupCount += 1
                continue
            
            if abs(nums[cur] - preValue) == 1:
                prePreNoTake, prePreTake,preTake, preNoTake = \
                preNoTake, preTake, nums[cur] * dupCount + max(prePreNoTake,prePreTake), max(preNoTake, preTake)
            else:
                prePreNoTake = preNoTake
                prePreTake = preTake
                preTake = max(preNoTake, preTake) + dupCount * nums[cur]
                preNoTake = preTake
            
            dupCount = 1
            preValue = nums[cur]
            cur += 1

        return max(preNoTake, preTake)
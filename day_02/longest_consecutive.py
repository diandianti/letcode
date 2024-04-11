from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        t = {}
        for n in nums:
            t[n] = 1

        longest = 0

        for n in t.keys():
            if n - 1 in t:
                continue
            cur_l = 1
            _t = n
            while _t + 1 in t:
                cur_l += 1
                _t += 1
            longest = cur_l if cur_l > longest else longest

        return longest

if __name__ == "__main__":
    in_nums = [4, 1, 2, 3]
    s = Solution()
    print(s.longestConsecutive(in_nums))

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        _d = {}
        for i in nums:
            _d[i] = _d.get(i, 0) + 1

        ts = []
        for key, v in _d.items():
            ts.append((key, v))

        ts = sorted(ts, key= lambda x:  -x[1])

        res = []
        for i in ts[:k]:
            res.append(i[0])

        return res

print(Solution().topKFrequent([3,0,1,0], 1))

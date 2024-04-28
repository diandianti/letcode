from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            tmp = []
            n = i + 1
            for j in range(n):
                if j == 0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(res[i - 1 ][j] + res[i - 1][j - 1])
            res.append(tmp)

        return res

print(Solution().generate(4))

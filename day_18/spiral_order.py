from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        lt = [0, 0]
        rb = [m, n]
        res = []

        cur = 0
        d = "r"
        count = m * n
        while count:
            for x in range(lt[1], rb[1]):
                res.append(matrix[cur][x])
                count -= 1
            lt[0] += 1
            cur = rb[1] - 1

            if count == 0: break

            for y in range(lt[0], rb[0]):
                res.append(matrix[y][cur])
                count -= 1
            rb[1] -= 1
            cur = rb[0] - 1
            if count == 0: break

            for x in range(rb[1] - 1, lt[1] - 1, -1):
                res.append(matrix[cur][x])
                count -= 1
            rb[0] -= 1
            cur = lt[1]
            if count == 0: break

            for y in range(rb[0] - 1, lt[0] - 1, -1):
                res.append(matrix[y][cur])
                count -= 1
            lt[1] += 1
            cur = lt[0]
            if count == 0: break

        return res

print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
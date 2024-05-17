from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] == target: return True
            if matrix[i][j] > target: i -= 1
            if matrix[i][j] < target: j += 1

        return False

print(Solution().searchMatrix([[2,5],[2,8],[7,9],[7,11],[9,11]], 7))
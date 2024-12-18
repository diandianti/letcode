#https://leetcode.cn/problems/minimum-path-sum/?envType=study-plan-v2&envId=dynamic-programming
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp = copy.deepcopy(grid)
        m, n = len(grid), len(grid[0])

        for i in range(m - 2, -1, -1):
            grid[i][-1] = grid[i + 1][-1] + grid[i][-1]
        
        for i in range(n - 2, -1, -1):
            grid[-1][i] = grid[-1][i + 1] + grid[-1][i]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                grid[i][j] = min(grid[i + 1][j], grid[i][j + 1]) + grid[i][j]

        return grid[0][0]
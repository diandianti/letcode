from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if i < 0 or j < 0:
                return
            if i >= n or j >=m:
                return
            if visit[j][i] == 1:
                return
            if grid[j][i] == "0":
                return

            visit[j][i] = 1
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for j in range(m):
            for i in range(n):
                if grid[j][i] == "1" and visit[j][i] == 0:
                    count += 1
                    dfs(i, j)

        return count

print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
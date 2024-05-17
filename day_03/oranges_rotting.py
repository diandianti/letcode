from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queues = [[], []]
        cur = 0
        queue = queues[cur]

        ok_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    ok_count += 1

        if ok_count == 0:
            return 0

        def mark(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if grid[i][j] != 1:
                return False
            grid[i][j] = 2
            return True

        count = -1
        while queues[cur] or queues[not cur]:
            queue = queues[cur]
            oq = queues[not cur]
            i, j = queue.pop(0)

            if mark(i + 1, j): oq.append((i + 1, j))
            if mark(i - 1, j): oq.append((i - 1, j))
            if mark(i, j + 1): oq.append((i, j + 1))
            if mark(i, j - 1): oq.append((i, j - 1))

            if not queue:
                count += 1
                cur = not cur

        for i in grid:
            for j in i:
                if j == 1:
                    count = -1

        return count

print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
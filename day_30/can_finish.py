import copy
from typing import List

#https://leetcode.cn/problems/course-schedule/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for i in range(numCourses)]
        for i, j in prerequisites:
            g[i].append(j)

        v = [0] * numCourses
        def dfs(i):
            if v[i] == 1:
                return False
            if v[i] == 2:
                return True

            v[i] = 1
            for dep in g[i]:
                if not dfs(dep):
                    return False
            v[i] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

print(Solution().canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
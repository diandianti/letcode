#https://leetcode.cn/problems/unique-paths/?envType=study-plan-v2&envId=dynamic-programming

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = []
        for i in range(m):
            dp.append([0 for j in range(n)])
        
        for i in range(m-1, -1, -1):
            dp[i][-1] = 1
        
        for i in range(n - 1, -1, -1):
            dp[-1][i] = 1
        

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        
        return dp[0][0]

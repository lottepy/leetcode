class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[m-1][n-1] = grid[m-1][n-1]
        for k in range(min(m,n)):
            if k == 0:    
                for i in range(m-2,-1,-1):
                    dp[i][n-1] = grid[i][n-1] + dp[i+1][n-1]
                for j in range(n-2,-1,-1):
                    dp[m-1][j] = grid[m-1][j] + dp[m-1][j+1]
            else:
                dp[m-1-k][n-1-k] = min(dp[m-1-k][n-k], dp[m-k][n-1-k]) + grid[m-1-k][n-1-k]
                for i in range(m-1-k,-1,-1):
                    dp[i][n-1-k] = min(dp[i+1][n-1-k], dp[i][n-k]) + grid[i][n-1-k]
                for j in range(n-1-k,-1,-1):
                    dp[m-1-k][j] = min(dp[m-1-k][j+1], dp[m-k][j]) + grid[m-1-k][j]

        return dp[0][0]
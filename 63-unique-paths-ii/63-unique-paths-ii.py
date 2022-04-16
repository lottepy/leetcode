class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # # Method 1: dp iteration
        # if len(sum(obstacleGrid, [])) < 1:
        #     return 0

        # if obstacleGrid[0][0] == 1:
        #     return 0

        # if obstacleGrid == [[0]]:
        #     return 1
        # elif obstacleGrid == [[1]]:
        #     return 0    

        # # Down
        # down = self.uniquePathsWithObstacles(obstacleGrid[1:])
        # # Right 
        # right = self.uniquePathsWithObstacles([sub[1:] for sub in obstacleGrid]) 

        # return down + right     

        # Method 2: dp tabulation
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        if obstacleGrid[m-1][n-1] == 1:
            return 0

        dp[m-1][n-1] = 1
        for k in range(min(m,n)):
            if k != 0:
                dp[m-1-k][n-1-k] = 0 if obstacleGrid[m-1-k][n-1-k]==1 else dp[m-1-k][n-k]+dp[m-k][n-1-k]
                for i in range(m-1-k,-1,-1):
                    dp[i][n-1-k] = 0 if obstacleGrid[i][n-1-k]==1 else dp[i+1][n-1-k]+dp[i][n-k]
                for j in range(n-1-k,-1,-1):
                    dp[m-1-k][j] = 0 if obstacleGrid[m-1-k][j]==1 else dp[m-1-k][j+1]+dp[m-k][j]
            if k == 0:    
                for i in range(m-2,-1,-1):
                    dp[i][n-1] = 0 if obstacleGrid[i][n-1]==1 else dp[i+1][n-1]
                for j in range(n-2,-1,-1):
                    dp[m-1][j] = 0 if obstacleGrid[m-1][j]==1 else dp[m-1][j+1]

        return dp[0][0] 
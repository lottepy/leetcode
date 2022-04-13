class Solution:
    def uniquePaths(self, m: int, n: int, memo=dict()) -> int:
        if (m,n) in memo:
            return memo[(m,n)]
        if n < 1 or m < 1:
            memo[(m,n)] = 0
            return 0
        elif n==1 and m==1:
            memo[(m,n)] = 1
            return 1
        elif m == 1 and n == 2:
            memo[(m,n)] = 1
            return 1
        elif n < m:
            return self.uniquePaths(n, m)    


        memo[(m,n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)    
        return memo[(m,n)]
        
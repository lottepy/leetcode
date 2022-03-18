class Solution:
    def climbStairs(self, n: int, memo = dict()) -> int:
        if n in memo:
            return memo[n]
        if n == 1:
            memo[1] = 1
            return 1
        elif n == 2:
            memo[2] = 2
            return 2    
        
        memo[n] = self.climbStairs(n-2, memo) + self.climbStairs(n-1, memo) 
        return memo[n]
class Solution:
    def jump(self, nums: List[int]) -> int:
        # # Method 1: Dynamic Programming
        # dp = list(range(len(nums)))
        # for i in range(len(nums)):
        #     for step in range(1, nums[i]+1):
        #         if i + step < len(nums):
        #             dp[i+step] = min(dp[i+step], dp[i]+1)              
        # return dp[-1]            

        # Method 2: Greedy
        res = 0
        l, r = 0, 0
        while r < len(nums) - 1:
            nextRight = 0
            for i in range(l, r+1):
                nextRight = max(nextRight, i+nums[i])
            l, r = r+1, nextRight
            res += 1    
        return res
        
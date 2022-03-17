class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = list(range(len(nums)))
        for i in range(len(nums)):
            for step in range(1, nums[i]+1):
                if i + step < len(nums):
                    dp[i+step] = min(dp[i+step], dp[i]+1)  
        return dp[-1] 
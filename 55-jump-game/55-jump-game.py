class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # # Method 1: dp
        # if len(nums) == 1:
        #     return True
        
        # dp = [False for _ in range(len(nums))]
        # dp[0] = True if nums[0] > 0 else False
        # for i in range(len(nums)):
        #     if dp[i]:
        #         for step in range(1,nums[i]+1):
        #             if i+step < len(nums):
        #                 dp[i+step] = True
        # return dp[len(nums)-1]     

        # Method 2: greedy
        if len(nums) == 1:
            return True
        _max = 0
        for i in range(len(nums)):
            if _max >= i:
                _max = max(_max, i + nums[i])
            else:
                break
        return _max >= len(nums) - 1        
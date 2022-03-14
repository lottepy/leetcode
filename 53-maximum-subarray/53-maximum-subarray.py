class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # Method 1: Accumulator
        # accu = 0
        # res = sum(nums)
        # _min = 0
        # for i in range(len(nums)):
        #     _min = min(accu, _min)
        #     accu += nums[i]
        #     res = max(res, accu - _min)

        # return res     

        # Method 2: sliding window
        cur = 0
        res = nums[0]
        for n in nums:
            if cur < 0:
                cur = 0
            cur += n   
            res = max(res, cur)     
        return res    
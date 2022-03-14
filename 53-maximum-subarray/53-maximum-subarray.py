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

        # # Method 2: sliding window
        # cur = 0
        # res = nums[0]
        # for n in nums:
        #     if cur < 0:
        #         cur = 0
        #     cur += n   
        #     res = max(res, cur)     
        # return res    

        # Method 3: D&C
        if len(nums) == 1:
            return nums[0]

        def crossMax(myArr):
            _max = myArr[0] 
            _sum = 0   
            for i in range(len(myArr)):
                _sum += myArr[i]
                _max = max(_max, _sum)
            return _max

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        leftMax = self.maxSubArray(left)
        rightmax = self.maxSubArray(right)
        midMax = crossMax(right) + crossMax(left[::-1])
        return max([leftMax, rightmax, midMax])

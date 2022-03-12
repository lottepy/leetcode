class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        accu = 0
        res = sum(nums)
        _min = 0
        for i in range(len(nums)):
            _min = min(accu, _min)
            accu += nums[i]
            res = max(res, accu - _min)

        return res     
            
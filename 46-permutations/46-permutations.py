class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        elif len(nums) == 2:
            return [nums, nums[::-1]]

        res = []
        for i in range(len(nums)):
            res += [[nums[i]] + l for l in self.permute(nums[:i] + nums[i+1:])]
        return res    
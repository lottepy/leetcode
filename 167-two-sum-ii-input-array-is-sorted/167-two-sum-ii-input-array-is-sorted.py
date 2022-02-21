class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = dict()
        for i in range(len(nums)):
            if nums[i] in hash:
                return [hash[nums[i]], i+1]
            else:    
                hash[target - nums[i]] = i + 1
        return []        
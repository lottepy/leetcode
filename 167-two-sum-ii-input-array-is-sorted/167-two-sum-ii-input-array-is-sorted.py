class Solution:
    # # Method 1: hash
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     hash = dict()
    #     for i in range(len(nums)):
    #         if nums[i] in hash:
    #             return [hash[nums[i]], i+1]
    #         else:    
    #             hash[target - nums[i]] = i + 1
    #     return []   

    # Method 2: Two pointers
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l, r = 0, len(nums)-1
        while l < r:
            _sum = nums[l] + nums[r]
            if _sum < target:
                l += 1
            elif _sum > target:
                r -= 1
            else:
                return [l+1, r+1]    
        return []         
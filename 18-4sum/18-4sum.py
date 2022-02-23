class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums)):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    _nums = [nums[k] for k in [i, j, l, r]]
                    _nums.sort()
                    _sums = sum(_nums) 
                    if _sums == target and _nums not in res:
                        res.append(_nums)
                        l += 1
                        while l < r and nums[l-1] == nums[l]:
                            l += 1
                    elif _sums <= target:
                        l += 1
                        while l < r and nums[l-1] == nums[l]:
                            l += 1
                    else:
                        r -= 1        
        return res              

if __name__ == '__main__':
    print(Solution().fourSum([1,0,-1,0,-2,2], 0))
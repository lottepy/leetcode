class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)    
        
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r    
            mid = (nums[l] + nums[r]) / 2
            if mid > target:
                r -= 1
            else:
                l += 1

        if nums[l] < target:
            return l + 1
        else:
            return l    
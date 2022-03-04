class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or target < nums[0] or target > nums[-1]:
            return [-1, -1]

        l, r = 0, len(nums) - 1
        _min, _max = -1, -1
        while l <= r:
            if nums[l] == target:          
                _min = l
            if nums[r] == target:
                _max = r

            if _min != -1 and _max != -1:
                return [_min, _max]
            elif _min != -1 and _max == -1:
                r -= 1
            elif _min == -1 and _max != -1:   
                l += 1  
            else: # _min = _max = -1      
                mid = (nums[l] + nums[r])
                if mid > target:
                    r -= 1
                else:
                    l += 1
        return [_min, _max]
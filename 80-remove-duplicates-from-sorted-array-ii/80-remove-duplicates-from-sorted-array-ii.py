class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = len(nums)

        prev = nums[0]
        count = 1
        i = 1
        while i < res:
            if nums[i] == prev:
                count += 1
                if count > 2:
                    nums[i-1:res-1] = nums[i:res]
                    res -= 1
                    i -= 1
            else:
                count = 1
                prev = nums[i]   
            i += 1     
        return res        
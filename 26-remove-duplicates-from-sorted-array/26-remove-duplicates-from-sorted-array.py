class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # # Method 1: sort
        # duplicates, i = 0, 1
        # curr = nums[0]
        # while i < len(nums):
        #     next = nums[i]
        #     if next == curr:
        #         duplicates += 1
        #         nums[i] = 101
        #     else:
        #         curr = next    
        #     i += 1    
        # nums.sort()        
        # return len(nums) - duplicates        

        # Method 2: no sort
        k = 0
        for i in range(len(nums)):
            if nums[i] != nums[k]:
                k += 1    
                nums[k] = nums[i]
        return k+1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates, i = 0, 1
        curr = nums[0]
        while i < len(nums):
            next = nums[i]
            if next == curr:
                duplicates += 1
                nums[i] = 101
            else:
                curr = next    
            i += 1    
        nums.sort()        
        return len(nums) - duplicates  
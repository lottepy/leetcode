class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set([n for n in nums if n > 0]))
        nums.sort(reverse=False)
        for i, n in enumerate(nums):
            if i+1 != nums[i]:
                return i +1

        return len(nums) + 1  
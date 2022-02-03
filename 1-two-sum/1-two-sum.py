class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counterNums = [target - i for i in nums]
        result = []
        for i, num in enumerate(counterNums):
            if num in nums:
                counterIdx = nums.index(num)
                if i != counterIdx:
                    return [i, counterIdx]
            
if __name__ == '__main__':
    sol = Solution()
    sol.twoSum([2,7,11,15], 9)
        
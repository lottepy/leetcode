class Solution:
    # # Hint 2
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     counterNums = [target - i for i in nums]
    #     result = []
    #     for i, num in enumerate(counterNums):
    #         if num in nums:
    #             counterIdx = nums.index(num)
    #             if i != counterIdx:
    #                 return [i, counterIdx]
    
    
    # # Hint 3
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        for i, num in enumerate(nums):
            residual = target - num
            if residual in list(hashMap.keys()):
                return sorted([i, hashMap[residual]], reverse=False)
            else:
                hashMap[num] = i
            
if __name__ == '__main__':
    sol = Solution()
    sol.twoSum([2,7,11,15], 9)
        
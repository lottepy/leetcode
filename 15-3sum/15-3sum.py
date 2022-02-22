
import copy
class Solution:
    # # Method 1: Brute Force
    # def threeSum(self, nums: list[int]) -> list[list[int]]:
    #     n = len(nums)
    #     if n < 3:
    #         return []
    #     res = dict()
    #     hash = dict()
    #     for i in range(n):
    #         for j in range(i+1, n):
    #             twoSum = nums[i] + nums[j]
    #             if twoSum not in hash:
    #                 hash[twoSum] = []
    #             hash[twoSum].append([i, j])

    #     for i in range(n):
    #         try:
    #             twoSum = copy.deepcopy(hash[-nums[i]])
    #             for pair in twoSum:
    #                 if i not in pair:
    #                     pair.append(i)
    #                     pair = [nums[j] for j in pair]
    #                     pair.sort()
    #                     res[tuple(pair)] = 0
    #         except:
    #             continue   
    #     return list([list(t) for t in res.keys()])    

    # # Method 2: Sort and TwoSum
    # def threeSum(self, nums: list[int]) -> list[list[int]]:
    #     def twoSum(_nums: list[int], target: int, i: int) -> list[list[int]]:
    #         _nums.pop(i)
    #         _hash = dict()
    #         _res = []
    #         for i in range(len(_nums)):
    #             if _nums[i] in _hash:
    #                 _res.append([_hash[_nums[i]], _nums[i]])
    #             else:
    #                 _hash[target - _nums[i]] = _nums[i]   
    #         return _res       

    #     res = dict()
    #     nums.sort()
    #     targetPool = set()
    #     for i, num in enumerate(nums):
    #         target = -num
    #         if target not in targetPool:
    #             targetPool.add(target)
    #             meetTarget = twoSum(copy.deepcopy(nums), target, i)
    #             if len(meetTarget) > 0:
    #                 for meet in meetTarget:
    #                     meet.append(num)
    #                     meet.sort()
    #                     res[tuple(meet)] = 0        
    #         else:
    #             continue            

    #     return [list(k) for k in res.keys()]

    # Method 3: Sort and Two Pointers
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        
        res = []
        i = 0
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums) - 1
            target = - nums[i]
            while left < right:
                if left == i:
                    left += 1
                if right == i:
                    right -= 1          
                if nums[left] + nums[right] == target:
                    res.append([nums[left], nums[right], nums[i]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1 
                elif nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1 
        return res
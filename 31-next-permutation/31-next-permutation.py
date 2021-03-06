import itertools
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def descend(l):
            if l == sorted(l, reverse=True):
                return True
            else:
                return False    

        for i in range(len(nums)):
            if descend(nums[i:]) and i == 0:
                nums.sort()
                return None
            elif descend(nums[i:]) and i > 0:
                anchor = nums[i]
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        anchor = nums[j]
                        break
                nums[j] = nums[i-1]
                nums[i-1] = anchor
                temp = nums[i:][::-1]
                for j in range(i, len(nums)):
                    nums[j] = temp[j-i]
                return None
            else:
                continue

        nums.sort() 
        return None 

        
if __name__ == '__main__':
    print(Solution().nextPermutation([1,5,1]))
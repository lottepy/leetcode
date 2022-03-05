class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # # Method 1: Two Binary Search
        def binary(li, target):
            l, r = 0, len(li)-1
            while l <= r:
                m = (l + r) // 2
                if li[m] < target:
                    l = m + 1
                elif li[m] > target:
                    r = m - 1   
                else:
                    return m 
            return -1 

        if len(nums) == 1:
            return -1 if nums[0] != target else 0
        rotation = False    
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                rotation = True
                break      

        # if rotation:
        #     upper = binary(nums[:i+1], target)    
        #     if upper != -1:
        #         return upper
        #     else:
        #         lower = binary(nums[i+1:], target)    
        #         if lower != -1:
        #             return i + lower + 1
        #         else:
        #             return -1        
        # else:
        #     return binary(nums, target)  

        # Method 2: One Binary Search
        if rotation:
            if target >= nums[0]:
                return binary(nums[:i+1], target)
            else:
                temp = binary(nums[i+1:], target) 
                return -1 if temp == -1 else temp + i + 1
        else:
            return binary(nums, target)          

        
if __name__ == '__main__':
    print(Solution().search([3],3))

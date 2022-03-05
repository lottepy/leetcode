class Solution:
    def search(self, nums: list[int], target: int) -> int:
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
                # nums = nums[i+1:] + nums[:i+1] 
                rotation = True
                break      

        if rotation:
            upper = binary(nums[:i+1], target)    
            lower = binary(nums[i+1:], target)
            if upper != -1:
                return upper
            elif lower != -1:
                return i + lower + 1
            else:
                return -1        
        else:
            return binary(nums, target)         

        
if __name__ == '__main__':
    print(Solution().search([3],3))

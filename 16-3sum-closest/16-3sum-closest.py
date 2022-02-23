class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        if len(nums) < 3:
            return []
        nums.sort()
        res = sum([smallest for smallest in nums[:3]])
        for i, t in enumerate(nums):
            # if i == 0 and nums[i] > target:
            #     break
            if i > 0 and t == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                _sum = t + nums[l] + nums[r]
                if _sum > target:
                    r -= 1
                elif _sum < target:
                    l += 1
                else:
                    return target  
                res = res if abs(res - target) < abs(_sum - target) else _sum          
        return res               

if __name__ == '__main__':
    print(Solution().threeSumClosest([-100,-98,-2,-1], -101))
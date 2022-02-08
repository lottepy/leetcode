class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # # Method 1: Queue Pop
        # while(len(nums1) + len(nums2) > 2):
        #     if len(nums1) == 0:
        #         left = nums2[0]
        #         right = nums2[-1]
        #     elif len(nums2) == 0:
        #         left = nums1[0]
        #         right = nums1[-1]
        #     else:   
        #         left = min(nums1[0], nums2[0])
        #         right = max(nums1[-1], nums2[-1])
        #     try:
        #         nums1.remove(left)
        #     except Exception:
        #         nums2.remove(left)    

        #     try:
        #         nums1.remove(right)
        #     except Exception:
        #         nums2.remove(right)        

        # if len(nums1) + len(nums2) == 2:
        #     return (sum(nums1) + sum(nums2)) / 2.0
        # else:
        #     return (sum(nums1) + sum(nums2))
        
        # Method 2: Binary Search

        def right(k, l):
            return float('inf') if k == len(l) or len(l) == 0 else l[k]

        def left(k, l):
            return -float('inf') if k == 0 or len(l) == 0 else l[k-1]
 

        n = len(nums1)
        m = len(nums2)
        if m < n:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = n
        _sum = n + m

        while low <= high:
            mid1 = int((low + high) // 2)
            mid2 = int((_sum + 1) // 2 - mid1)
            if left(mid2, nums2) <= right(mid1, nums1) and left(mid1, nums1) <= right(mid2, nums2):
                    return max(float(left(mid1, nums1)), float(left(mid2, nums2))) if _sum % 2 == 1 else (max(left(mid1, nums1), left(mid2, nums2)) + min(right(mid1, nums1), right(mid2, nums2))) / 2.0
       
            elif left(mid2, nums2) > right(mid1, nums1):
                low = mid1 + 1
            else:    
                high = mid1 - 1
        return -1            

   
    

if __name__ == '__main__':
    nums1, nums2 = [], [1]
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))
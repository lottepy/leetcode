class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        while(len(nums1) + len(nums2) > 2):
            if len(nums1) == 0:
                left = nums2[0]
                right = nums2[-1]
            elif len(nums2) == 0:
                left = nums1[0]
                right = nums1[-1]
            else:   
                left = min(nums1[0], nums2[0])
                right = max(nums1[-1], nums2[-1])
            try:
                nums1.remove(left)
            except Exception:
                nums2.remove(left)    

            try:
                nums1.remove(right)
            except Exception:
                nums2.remove(right)        

        if len(nums1) + len(nums2) == 2:
            return (sum(nums1) + sum(nums2)) / 2.0
        else:
            return float(list(set(nums1).union(set(nums2)))[0])


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMedianSortedArrays([1,3], [2]))
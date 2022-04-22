class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return None
        if m == 0:
            nums1[:] = nums2
            return None

        if nums1[0] > nums2[0]:
            nums1[1:m+1] = nums1[:m]
            nums1[0] = nums2[0]
            j = 1
            end = m + 1
        else:
            j = 0
            end = m
        i = 1
        while i < m + n and end < m + n:
            if nums2[j] >= nums1[i]:
                i += 1
                continue
            elif nums2[j] < nums1[i]:
                nums1[i+1:end+1] = nums1[i:end]
                nums1[i] = nums2[j]
                j += 1
                end += 1
                i += 1
        if end != m+n:
            nums1[end:] = nums2[j:]
        return None
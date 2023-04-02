class Solution(object):
    def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        half = total // 2


        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            nums1_left = float(nums1[i] if i >= 0 else float('-inf'))
            nums1_right = float(nums1[i+1] if i+1 < len(nums1) else float('inf'))
            nums2_left = float(nums2[j] if j >= 0 else float('-inf'))
            nums2_right = float(nums2[j+1] if j+1 < len(nums2) else float('inf'))

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                else:
                    return max(nums1_left, nums2_left)
            elif nums1_left > nums2_right:
                r = i - 1
            else:
                l = i + 1
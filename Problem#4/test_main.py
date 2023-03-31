import pytest

from main import Solution

def test_use_case_proper_value_first() -> None:
    nums1 = [1,3]
    nums2 = [2]
    output = Solution.findMedianSortedArrays(nums1,nums2)
    assert output == 2.0

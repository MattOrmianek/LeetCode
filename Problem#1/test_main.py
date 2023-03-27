import pytest

from main import Solution

def test_use_case_proper_value_first() -> None:
    indexes = Solution.twoSum([2,7,11,15],9)
    assert indexes == [0,1]

def test_use_case_proper_value_second() -> None:
    indexes = Solution.twoSum([3,2,4],6)
    assert indexes == [1,2]

def test_use_case_proper_value_third() -> None:
    indexes = Solution.twoSum([3,3],6)
    assert indexes == [0,1]
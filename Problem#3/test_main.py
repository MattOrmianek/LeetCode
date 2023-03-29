import pytest

from main import Solution

def test_use_case_proper_value_first() -> None:
    s = "abcabcbb"
    output = Solution.lengthOfLongestSubstring(s)
    assert output == 3

def test_use_case_proper_value_second() -> None:
    s = "bbbbb"
    output = Solution.lengthOfLongestSubstring(s)
    assert output == 1
def test_use_case_proper_value_third() -> None:
    s = "pwwkew"
    output = Solution.lengthOfLongestSubstring(s)
    assert output == 3

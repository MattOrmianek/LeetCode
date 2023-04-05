import pytest

from main import Solution

def test_use_case_proper_value_first() -> None:
    assert Solution().longestPalindrome("babad") == "aba"

def test_use_case_proper_value_second() -> None:
    assert Solution().longestPalindrome("cbbd") == "bb"
import pytest

from main import Solution

def test_use_case_proper_value_first() -> None:
    list_1 = [2,4,3]
    list_2 = [5,6,7]
    output = Solution.addTwoNumbers(list_1,list_2)
    assert output == [7,0,8]

def test_use_case_proper_value_second() -> None:
    list_1 = [0]
    list_2 = [0]
    output = Solution.addTwoNumbers(list_1,list_2)
    assert output == [0]

def test_use_case_proper_value_third() -> None:
    list_1 = [9,9,9,9,9,9,9]
    list_2 = [9,9,9,9]
    output = Solution.addTwoNumbers(list_1,list_2)
    assert output == [8,9,9,9,0,0,0,1]
import pytest

from fractions import Fraction
from my_sum.my_sum import my_sum_func

def test_list_int():
    """
    Test that it can sum a list of integers
    """
    data = [1, 2, 3]
    assert my_sum_func(data) == 6

def test_tuple_int():
    """
    Test that it can sum a tuple of integers
    """
    data = (1, 2, 3)
    assert my_sum_func(data) == 6

def test_fraction():
    """
    Test that it can sum a tuple of integers
    """
    data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 4)]
    print(my_sum_func(data))
    assert my_sum_func(data) == 1

def test_zero_sum():
    """
    Test that it can sum a tuple of integers
    """
    data = [-2, 1, 1]
    assert my_sum_func(data) == 0

def test_bad_type():
    data = 'banana'
    with pytest.raises(TypeError):
        my_sum_func(data)

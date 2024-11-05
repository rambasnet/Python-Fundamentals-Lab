"""Modue to test file_io.py
"""

import file_io


def test_sort_ascending1() -> None:
    """Test sort_list_ascending_order function.
    """
    my_nums = [10, 9, 0, -6]
    file_io.sort_list_ascending_order(my_nums)
    assert (my_nums == [-6, 0, 9, 10])

# add 3 more test cases in separate test functions


def test_sort_descending1() -> None:
    """Test sort_list_descending_order function.
    """
    my_nums = [0, -10, -1, 5, 100]
    file_io.sort_list_descending_order(my_nums)
    assert my_nums == [100, 5, 0, -1, -10]


# add 3 more test cases in seeparate test functions

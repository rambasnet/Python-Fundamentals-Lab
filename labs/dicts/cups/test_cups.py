"""Unit test module for cups
"""

from cups import sort_cups


def test_sort_cups_1() -> None:
    """test if the cups are sorted correclty.
    """
    cups = {100: 'red', 10: 'blue', 50: 'yellow'}
    sorted_cups = sort_cups(cups)
    expected = ['blue', 'yellow', 'red']
    assert sorted_cups == expected


# FIXME6 : add a unit test function
# FIXME7 : add a unit test function
# FIXME8 : add a unit test function
# FIXME9 : add a unit test function
# FIXME10 : add a unit test function

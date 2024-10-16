"""Module to test important functions in twostones.py
"""

import twostones
# test function must start with test_ prefix for pytest to recognize it


def test_odd_even():
    """Function to test odd_even function
    """
    number = 99999
    expected = "odd"
    ans = twostones.odd_even(number)
    assert (ans == expected), f"Expected: {expected}, but got: {ans}"


def test_odd_even2():
    """Function to test odd_even function"""
    assert (twostones.odd_even(200) ==
            "even"), f"Expected: even, but got: {twostones.odd_even(200)}"


# FIXME 5: Write 3rd test case
# FIXME 6: Write 4th test case


# FIXME 7: Write 3 test functions to test answer function

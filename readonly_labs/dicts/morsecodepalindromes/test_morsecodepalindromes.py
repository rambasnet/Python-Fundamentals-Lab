"""Module to test functions in morsecode.py 
"""

import morsecodepalindromes


def test_convert_to_morse() -> None:
    """Tests convert_to_morse function."""
    actual_ans = morsecodepalindromes.convert_to_morse('AN')
    expected_ans = '.--.'
    assert actual_ans == expected_ans

# FIXME 6 - write 3 more test funbctions with different cases
# to test convert_to_morse function


def test_ispalindrome1() -> None:
    """Tests is_palindrome function.
    """
    ans = morsecodepalindromes.is_palindrome('.--.')
    expected = 1
    assert ans == expected

# FIXME 7 - Write 3 more test functions with different cases
# to test is_palindrome function

"""Module to test functions from main.py
"""

import sys
import thelastproblem as lastproblem

# Note: test function must start with test_ prefix for pytest to find it


def test_answer():
    """Test answer function
    """
    ans = lastproblem.answer("Alice")
    expected = "Thank you, Alice, and farewell!"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    ans = lastproblem.answer("Bob")
    expected = "Thank you, Bob and farewell!"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    print("All two test cases passed...", file=sys.stderr)


def test_answer1():
    """Test answer1 function
    """
    # FIXME 7: add a new test case to test your answer function
    # FIXME 8: add a new test case to test your answer function
    # FIXME 9: add a new test case to test your answer function
    # FIXME 10: add a new test case to test your answer function

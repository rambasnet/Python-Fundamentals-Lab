"""Test module to test functions from edays.py
"""

from edays import answer


def test_answer():
    """Test answer function
    """
    ans = answer(10)
    expected = 20
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# Note: test function must start with test_ prefix for pytest to find it
# FIXME 7: Create a new test function with different test case
# FIXME 8: Create a new test function with different test case
# FIXME 9: Create a new test function with different test case
# FIXME 10: Create a new test function with different test case

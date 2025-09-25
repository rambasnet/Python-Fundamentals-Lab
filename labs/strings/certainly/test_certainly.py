"""Test module for certainly.py 
"""

from certainly import answer


def test_answer() -> None:
    """Testing the answer function for 1.
    """
    assert answer('of course! certainly is present.') == 1


# FIXME 5: add 3 more tests functions to test all the edge cases

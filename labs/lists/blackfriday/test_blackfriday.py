"""Test module for blackfriday.py
"""

from blackfriday import max_unique_index


def test_max_unique_index() -> None:
    """Test max_unique_index with a list of unique numbers in ascending order.
    """
    nums = [1, 2, 3]
    assert max_unique_index(nums) == 3


def test_max_unique_index_descending() -> None:
    """Test max_unique_index with a list of unique numbers in descending order.
    """
    nums = [3, 2, 1]
    assert max_unique_index(nums) == 1


def test_max_unique_index_no_unique() -> None:
    """Test max_unique_index with a list that has no unique numbers.
    """
    nums = [1, 2, 2, 1]
    assert max_unique_index(nums) == -1

# FIXME 5: Write at least three more test cases

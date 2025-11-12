"""Module for testing the hailstone_sum function."""

from hailstone import hailstone_sum


def test_hailstone_sum_1() -> None:
    """Teset hailstone_sum with input 1."""
    assert hailstone_sum(1) == 1


def test_hailstone_sum_2() -> None:
    """Test hailstone_sum with input 2."""
    input_value = 2
    expected = 2 + 1  # Sequence: 2, 1
    assert hailstone_sum(input_value) == expected


# FIXME5 - Write at least 3 more unit test functions
# to test hailstone_sum function

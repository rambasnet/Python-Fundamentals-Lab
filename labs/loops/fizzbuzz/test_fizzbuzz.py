"""Test module for fizzbuzz.py
"""

from fizzbuzz import fizzbuzz


def test_fizzbuzz() -> None:
    """Test the fizzbuzz function for FizzBuzz results with various inputs."""
    assert fizzbuzz(15, 3, 5) == "FizzBuzz"  # fixed
    assert fizzbuzz(30, 3, 5) == "FizzBuzz"  # fixed
    assert fizzbuzz(6, 2, 3) == "FizzBuzz"   # fixed


def test_fizz() -> None:
    """Test the fizzbuzz function for "Fizz" results with various inputs."""
    # FIXME 1: add at least 3 assert statments to check for "Fizz" results


# FIXME 2: write a test function with at least 3 assert statements
# to check for "Buzz" results

# FIXME 3: write a test function with at least 3 assert statements
# to check for number results

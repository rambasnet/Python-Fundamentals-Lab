"""
Lists and Unit tests - B
CSCI 110 Lab
Update by: FIXME
Date: FIXME

Solution to the Kattis problem: https://open.kattis.com/problems/blackfriday

Algorithm Steps:
1. read the input data into a list of integers
2. find the participant with the highest unique outcome
    a. iterate through the list and for each unique value, check if it's the highest
    b. keep track of the highest unique value and its index
3. if such a participant exists, print their index (1-based), otherwise print none
"""

import sys
from typing import List


def get_data() -> List[int]:
    """Reads the data from std input and returns it as a list of ints
    Args:
        None
    Returns:
        List[int]: list of ints
    """
    _ = input()  # read and ignore the first line
    nums = input().split()  # list of string numbers
    int_nums: List[int] = []
    # FIXME 1: using a for loop convert each string number in nums to int
    #  and append to int_nums
    return int_nums


def max_unique_index(data: List[int]) -> int:
    """Find the index of the participant that has the highest unique outcome.
    Args:
        data (List[int]): List of integers
    Returns:
        int: index of the participant with the highest unique outcome, or -1
    """
    max_index = -1
    max_value = -1
    for index, value in enumerate(data):
        if data.count(value) == 1:  # check if the value is unique
            pass
            # FIXME 2: if the value is greater than max_value,
            # update max_value and max_index with value and index

    # FIXME 3: if the max_index is not -1, return max_index + 1, else return -1
    return max_index


def main() -> None:
    """Main function that solves the problem
    """
    data: List[int] = get_data()
    # let's check if data is in right format
    print(f'{data=}', file=sys.stderr)
    result: int = max_unique_index(data)
    # FIXME 4: interpret result and print the answer


if __name__ == "__main__":
    main()

"""
Dictionary and Unittest Lab - B
Updated By: FIXME
CSCI 110 Lab
Date: FIXME

Kattis problem - Stacking Cups - https://open.kattis.com/problems/cups  

Sort the cups in order of increasing radius.

Algorithm steps:
1. Read the n - number of cups
2. Create a dictionary mapping radius to color
3. Repeat n times
    a. read a line and parse the input (diameter color or color radius)
    b. add radius as a key and color as value to the dictionary
4. Sort dictionary on keys using sorted function
5. Go through each sorted radius and add the corresponding color to a list
6. Print the list of color one per line
"""

import sys


def sort_cups(cups: dict) -> list:
    """Sorts the cups dict based on keys and returns the color.

    Args:
        cups (dict): dict with radius as key and color as corresponding value.

    Returns:
        list: list of sorted colors based on radius.
    """
    # sort the cups based on keys and get a sorted dict
    sorted_keys = sorted(cups)
    ans = []
    # FIXME4: traverse through sorted_keys and add the corresponding value to ans
    return ans


def main():
    # read the first line
    n = int(sys.stdin.readline().strip())
    # FIXME1: initialize cups as an empty dictionary
    cups = None
    for _ in range(n):
        # FIXME2 : read each line and split it into two variables
        # FIXME3 : add radius (int) as a key and color as a value to cups
        # Note. if the first variable is number, it must be diameter.
        # convert it into a radius before adding it to the cups.
        pass

    ans = sort_cups(cups)
    print(f'{ans=}', file=sys.stderr)
    # FIXME5: print the colors in ans one line at a time


if __name__ == '__main__':
    main()

"""
User-defined Functions Lab
Completed By: FIXME
CSCI 110 Lab
Date: FIXME

Solution to Kattis problem - Buka: https://open.kattis.com/problems/triarea

Algorithm steps:
  1. Create a function triarea() that takes base and height as
     parameters and returns the area of the triangle calculated using the
     formula (0.5 * base * height)
  2. read the 1st and only line of input containing height (h) and base (b)
  3. call triarea() with base and height and print the result
"""

import sys


def triarea(base: int, height: int) -> float:
    """
    Returns the area of a triangle given base and height.
    """
    # FIXME1: Write the formula to calculate area
    area = 0
    return area


def solve():
    """Main function that solves the problem"""
    # FIXME2: Read a line of input from stdin and split into base and height
    # Example input: "3 4"
    line = sys.stdin.readline().strip()  # same as input()
    # FIXME3: Split the line into two variables, base and height
    base, height = "FIXME"
    print(f'{base=}, {height=}', file=sys.stderr)  # Debug print
    # FIXME4: Convert base and height to integers or floats as needed
    base = "FIXME"
    height = "FIXME"
    # FIXME5: Call triarea() and print the returned result using sys.stdout.write()


# Call solve() function to execute it
solve()

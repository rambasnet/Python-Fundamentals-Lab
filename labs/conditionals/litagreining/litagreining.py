"""
Conditionals Lab
Updated By: FIXME
CSCI 110 Lab
Date: FIXME

Read and solve the Kattis problem: https://open.kattis.com/problems/litagreining 

Algorithm Steps:
  1. Read the RGB values using a function
  2. Classify the color based on the RGB values using a fruitful function
  3. Print the classification
"""

import sys


def read_rgb() -> tuple[int, int, int]:
    """Read a line from stdin and return a tuple of three integers (r, g, b).

    Returns:
        tuple[int, int, int]: A tuple of RGB values.
    """
    line = sys.stdin.readline().strip()
    r, g, b = line.split()
    return int(r), int(g), int(b)


def classify(r: int, g: int, b: int) -> str:
    """Return the color classification for given RGB integers."""
    # All equal cases
    if r == g == b:
        if r == 0:
            return "svartur"
        # FIXME 4: if r, g, and b are qual and r equals 255, return "hvitur"
        return "grar"

    # Single strictly largest
    if r > g and r > b:
        return "raudur"
    # FIXME 5: if g is strictly greater than both r and b, return "graenn"
    # FIXME 6: implement the condition to check for blar and return "blar"

    # Two equal and strictly greater than the third
    if r == g and r > b:
        return "gulur"
    # FIXME 7: if r and b are equal and greater than g, return "fjolubleikur"
    # FIXME 8: implement the condition to check for blagraenn and return "blagraenn"

    # FIXME 9: If none of the above is correct, return 'othekkt"
    return 'FIXME'


def main() -> None:
    """Main function to read RGB values, classify the color,
        and print the result.
    """
    r, g, b = read_rgb()
    print(classify(r, g, b))


if __name__ == "__main__":
    main()

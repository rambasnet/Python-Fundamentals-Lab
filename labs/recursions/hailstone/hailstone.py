#! /usr/bin/env python3

"""
Recursion Lab
Updated By: FIXME
CSCI 110 Lab
Date: FIXME

Read and solve the Kattis problem: https://open.kattis.com/problems/hailstone  

Algorithm Steps:
  1. Read the number n
  2. Implement a recursive function say h_s(n) to sum hailstone sequence from n to 1
    - base case: if n is 1, the sum is 1
    - general case1: if n is even, the sum is n+h_s(n//2)
    - FIXME1 - write the step for 2nd general case
  3. Print the sum returned by h_s(n)
"""


def hailstone_sum(n) -> int:
    """Generate the hailstone sequence starting at n.

    The hailstone sequence is defined as follows:
    - If n is 1, the sum is 1.
    - If n is even, the next number is n // 2.
    - If n is odd, the next number is 3 * n + 1.

    Args:
        n (int): The starting number of the hailstone sequence.

    Returns:
        int: The sum of the hailstone sequence starting at n.
    """
    # Base case
    # FIXME2: Handle base case
    if n == 1:
        return 0
    # First recursive general case
    elif n % 2 == 0:
        # add current and the next number
        return n + hailstone_sum(n // 2)
    else:
        # FIXME3: Implement 2nd recursive general case
        return 0


def main() -> None:
    """Main function to test hailstone sequence generation."""
    n = int(input())
    # FIXME4: Call hailstone_sum function and print the answer


if __name__ == "__main__":
    main()

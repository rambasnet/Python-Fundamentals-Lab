"""
Loops and Unittest Lab - B
Updated By: FIXME
CSCI 110 Lab
Date: FIXME

Read and solve - FizzBuzz: https://open.kattis.com/problems/fizzbuzz

Algorithm:
    1. Read X, Y, N
    2. Repeat from 1 to N:
        i. If the number is divisible by both X and Y, print "FizzBuzz"
        ii. If the number is divisible by X, print "Fizz"
        iii. If the number is divisible by Y, print "Buzz"
        iv. Otherwise, print the number
"""

import sys


def fizzbuzz(n: int, x: int, y: int) -> str:
    """Returns the FizzBuzz result for given x, y, and n.

    Args:
        n (int): the number to check
        x (int): first divisor
        y (int): second divisor


    Returns:
        str: "FizzBuzz" if n divisible by x and y,
             "Fizz" if n divisible by x,
             "Buzz" if n divisible by y,
             otherwise the number as a string
    """
    if n % x == 0 and n % y == 0:
        return "FizzBuzz"
    elif n % x == 0:
        return "Fizz"
    # FIXME 1: if n is divisible by y, return "Buzz"
    # FIXME 2: if none of the above, return the number n as a string
    return "FIXME"


def read_data() -> tuple[int, int, int]:
    """Reads X, Y, N from stdin and returns them as a tuple of integers.

    Returns:
        tuple[int, int, int]: A tuple containing X, Y, and N.
    """
    X, Y, N = sys.stdin.readline().strip().split()
    # FIXME 3: convert X, Y, N to integers and return as a tuple
    return 0, 0, 0


def solve(x: int, y: int, n: int) -> None:
    """Solves the FizzBuzz problem by reading input, processing it,
       and printing the results.
    """
    # FIXME 4: step 2. call fizz_buzz n+1 times from 1 to n
    # and print the results as shown in the sample output


def main() -> None:
    """Main function that solves the problem
    """
    # step 1. read data
    x, y, n = read_data()
    # step 2. solve the problem and print the results
    # FIXME 5: call the solve function passing x, y, n as arguments


if __name__ == "__main__":
    main()

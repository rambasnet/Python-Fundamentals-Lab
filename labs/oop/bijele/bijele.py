#! /usr/bin/env python3

"""
Using OOP concept, solve: Bijele - https://open.kattis.com/problems/bijele

Algorithm:
    1. Create chess.py module to define the the Chess class
        i. Define the __init__ method to initialize the Chess class
        ii. Define the __str__ method to return the string representation of the Chess class
        iii. Define the __sub__ method to return the difference between two Chess objects
    2. Create two chess objects - actual and found pieces
    3. print the difference as shown in the sample output
"""

__author__ = "FIXME"
__date__ = "FIXME"
__course__ = "CSCI 110 Lab"
__semester__ = "FIXME"
__lab__ = "OOP Lab - Bijele Problem"

from chess import Chess


def main() -> None:
    # the actual chess pieces count
    # chess has 1 king, 1 queen, 2 rooks, 2 bishops, 2 knights, and 8 pawns
    actual_chess: Chess = Chess(
        king=1, queen=1, rooks=2, bishops=2, knights=2, pawns=8)
    # FIXME - assign the pieces count from the input
    found_pieces = 0, 0, 0, 0, 0, 0  # replace with input reading logic
    # FIXME - create a Chess object using the input data
    found_chess: Chess = None
    # find the difference between the actual and input chess pieces count
    ans: Chess = actual_chess - found_chess  # creates a new Chess object
    # FIXME - print the answer


if __name__ == "__main__":
    main()

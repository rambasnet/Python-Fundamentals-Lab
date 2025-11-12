#! /usr/bin/env python3
"""
This module solves the trik problem.
https://open.kattis.com/problems/trik

Algorithm:
1. Define ThreeCupsGame class
2. Read the moves to simulate
3. Create an instance of the ThreeCupsGame class
    - initial position of the ball is in the left or cup 1
4. Iterate through all the moves to update the ball position
    a. If the move is 'A', call the move_a function
    b. If the move is 'B', call the move_b function
    c. Otherwise, call the move_c function
5. Print the final position of the ball
"""

__author__ = "FIXME"
__date__ = "FIXME"
__course__ = "CSCI 110 Lab"
__semester__ = "FIXME"
__lab__ = "OOP Lab - Trik Problem"

from three_cup import ThreeCupsGame


def main() -> None:
    """Main function that solves the problem.
    """
    # read the moves
    moves = input()
    # create an instance of the ThreeCupsGame class
    game = None  # FIXME1 - create the game object
    # iterate through the moves
    for move in moves:
        # call the corresponding move method
        if move == 'A':
            game.move_a()
        elif move == 'B':
            game.move_b()
        # FIXME2: otherwise, call the move_c method

    # print the final position of the ball
    # FIXME3: use game object to call the position getter method
    print(1)


if __name__ == '__main__':
    main()

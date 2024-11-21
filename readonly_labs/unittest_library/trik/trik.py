#! /usr/bin/env python3

"""
This module solves the trik problem.
https://open.kattis.com/problems/trik

Algorithm:
1. Read the moves.
2. Create an instance of the ThreeCupsGame class.
    - initial position of the ball is in the left or cup 1.
3. Iterate through all the moves to update the ball position.
    a. If the move is 'A', call the move_a function.
    b. If the move is 'B', call the move_b function.
    c. Otherwise, call the move_c function.

4. Print the final position of the ball.
"""

from three_cups_game import ThreeCupsGame


def main() -> None:
    """Main function that solves the problem.
    """
    # read the moves
    moves = input()
    # create an instance of the ThreeCupsGame class
    game = ThreeCupsGame()
    # iterate through the moves
    for move in moves:
        # call the corresponding move method
        if move == 'A':
            game.move_a()
        elif move == 'B':
            game.move_b()
        # FIXME 1: otherwise, call the move_c method

    # print the final position of the ball
    print(game.get_position())


if __name__ == '__main__':
    main()

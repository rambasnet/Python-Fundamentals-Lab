#! /usr/bin/env python3

"""
This module contains a class for solving the trik problem.
https://open.kattis.com/problems/trik

"""


class ThreeCupsGame:
    """Class to solve the trik problem.
    """

    def __init__(self) -> None:
        """Initializes the class with the initial position of the ball.
        """
        self.position = 1  # initial position of the ball

    def move_a(self) -> None:
        """Simulate move A where first two cups are moved.
        """
        if self.position == 1:
            self.position = 2
        elif self.position == 2:
            self.position = 1

    def move_b(self) -> None:
        """Simulate move B where second and third cups are moved.
        """
        if self.position == 2:
            self.position = 3
        elif self.position == 3:
            self.position = 2

    def move_c(self) -> None:
        """Simulate move C where first and third cups are moved.
        """
        # FIXME 1: implement the move_c function

    def get_position(self) -> int:
        """Returns the current position of the ball.

        Returns:
            int: the current position of the ball
        """
        return self.position

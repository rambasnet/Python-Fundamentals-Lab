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
        self._position = 1  # initial position of the ball

    def move_a(self) -> None:
        """Simulate move A where first two cups are moved.
        """
        if self._position == 1:
            self._position = 2
        elif self._position == 2:
            self._position = 1

    def move_b(self) -> None:
        """Simulate move B where second and third cups are moved.
        """
        if self._position == 2:
            self._position = 3
        elif self._position == 3:
            self._position = 2

    def move_c(self) -> None:
        """Simulate move C where first and third cups are moved.
        """
        # FIXME 1: implement the move_c function

    def get_position(self) -> int:
        """Returns the current position of the ball.

        Returns:
            int: the current position of the ball
        """
        return self._position

    @property
    def position(self) -> int:
        """Returns the current position of the ball.

        Returns:
            value (int): the current position of the ball
        """
        return self._position

    @position.setter
    def position(self, value: int) -> None:
        """Set the current position of the ball.

        Args:
            value (int): the current position of the ball
        """
        assert value in [1, 2, 3], 'Invalid position'
        self._position = value

#! /usr/bin/env python3

"""
This module contains a class for testing
the ThreeCupsGame class.
"""


import unittest
from three_cups_game import ThreeCupsGame


class TestThreeCupsGame(unittest.TestCase):
    """Test the ThreeCupsGame class.
    """

    def test__init__(self) -> None:
        """Test the __init__ method.
        """
        game = ThreeCupsGame()
        self.assertEqual(game.position, 1)

    def test_move_a1(self) -> None:
        """Test the move_a method.
        """
        game = ThreeCupsGame()
        game.move_a()
        self.assertEqual(game.position, 2)

    # FIXME : Add 1 test method to test the move_a method

    def test_move_b(self) -> None:
        """Test the move_b method.
        """
        game = ThreeCupsGame()
        game.move_a()
        self.assertEqual(game.position, 2)
        game.move_b()
        self.assertEqual(game.position, 3)

    # FIXME : Add 2 new test methods to test the move_b method

    def test_move_c(self) -> None:
        """Test the move_c method.
        """
        game = ThreeCupsGame()
        self.assertEqual(game.position, 1)
        game.move_b()
        self.assertEqual(game.position, 2)
        game.move_c()
        self.assertEqual(game.position, 3)

    # FIXME : Add 2 new test methods to test the move_c method

    def test_get_position(self) -> None:
        """Test the get_position method.
        """
        game = ThreeCupsGame()
        self.assertEqual(game.get_position(), 1)

    # FIXME : Add 2 new test methods to test the get_position method

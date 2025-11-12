""" Test module for ThreeCupsGame class. """

from unittest import TestCase
from three_cup import ThreeCupsGame


class TestThreeCupsGame(TestCase):
    """Test class for ThreeCupsGame.
        Class inherits from unittest.TestCase
        you get access to all the assertion methods
    """

    def test_initial_position(self) -> None:
        """Test that the initial position of the ball is under cup 1."""
        game = ThreeCupsGame()
        self.assertEqual(game.get_position(), 1)

    def test_move_a(self) -> None:
        """Test move_a method."""
        game = ThreeCupsGame()
        game.move_a()
        self.assertEqual(game.get_position(), 2)
        game.move_a()
        self.assertEqual(game.get_position(), 1)

    # FIXME3 - Write at least 3 more unit test methods
    # must use inheritated methods to assert the correctness of
    # move_b, move_c, and a sequence of moves

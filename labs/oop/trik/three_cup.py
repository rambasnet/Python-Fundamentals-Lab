"""Class to represent three cup game.
"""


class ThreeCupsGame:
    """ThreeCupsGame class to represent the three cup game.
    The ball starts under cup 1.
    """

    def __init__(self) -> None:
        """Initialize the game with the ball under cup 1.
        """
        self.position = 1

    def move_a(self) -> None:
        """Swap cups 1 and 2.
        """
        if self.position == 1:
            self.position = 2
        elif self.position == 2:
            self.position = 1

    def move_b(self) -> None:
        """Swap cups 2 and 3.
        """
        # FIXME4: implement the method to swap cups 2 and 3

    def move_c(self) -> None:
        """Swap cups 1 and 3.
        """
        # FIXME5: implement the method to swap cups 1 and 3

    def get_position(self) -> int:
        """Get the current position of the ball.

        Returns:
            int: The current position of the ball (1, 2, or 3).
        """
        return self.position

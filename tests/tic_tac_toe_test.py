"""Unit-Testing for the text-based Tic-Tac-Toe game."""

import unittest
from tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    """Test Case Class"""
    def test_canary(self):
        """Canary test to make sure everything is working."""
        self.assertTrue(1+1, 2)

    def test_init_game(self):
        """Initializing to an empty game board/state."""
        game = TicTacToe()
        self.assertEqual(game.get_game_state(), [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])


# Use only if you are testing directly from running this file.
if __name__ == "__main__":
    unittest.main()

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

    def test_one_move(self):
        """Check the state of the game after Player 1 makes their first move."""
        game = TicTacToe()
        game.place_piece("b2")
        self.assertEqual(game.get_game_state(), [['-', '-', '-'], ['-', '-', 'X'], ['-', '-', '-']])

    def test_two_moves(self):
        """Check the state of the game after Player 1 & 2 make their first moves."""
        game = TicTacToe()
        game.place_piece("b2")
        game.place_piece("a0")
        self.assertEqual(game.get_game_state(), [['O', '-', '-'], ['-', '-', 'X'], ['-', '-', '-']])

    def test_conflicting_move(self):
        """Check the state of the game after PLayer 2 tries to claim Player 1's cell."""
        game = TicTacToe()
        game.place_piece("b2")
        game.place_piece("a0")
        status = "BAD" if not game.place_piece("a0") else "OK"
        self.assertEqual(status, "BAD")
        self.assertEqual(game.get_game_state(), [['O', '-', '-'], ['-', '-', 'X'], ['-', '-', '-']])

# Use only if you are testing directly from running this file.
if __name__ == "__main__":
    unittest.main()

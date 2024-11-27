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
        self.assertEqual(game.current_player, 1)
        self.assertEqual(game.get_game_state(), [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])

    def test_one_move(self):
        """Check the state of the game after Player 1 makes their first move."""
        game = TicTacToe()
        game.place_piece("b2")
        self.assertEqual(game.get_game_state(), [['-', '-', '-'], ['-', '-', 'X'], ['-', '-', '-']])

    def test_player_change(self):
        """Check that the current player (1 or 2) is getting set properly"""
        game = TicTacToe()
        self.assertEqual(game.current_player, 1)
        game.next_player()
        self.assertEqual(game.current_player, 2)

    def test_two_moves(self):
        """Check the state of the game after Player 1 & 2 make their first moves."""
        game = TicTacToe()
        game.place_piece("b2")
        game.next_player()
        game.place_piece("a0")
        self.assertEqual(game.get_game_state(), [['O', '-', '-'], ['-', '-', 'X'], ['-', '-', '-']])

    def test_conflicting_move(self):
        """Check the state of the game after Player 2 tries to claim Player 1's cell."""
        game = TicTacToe()
        game.place_piece("b2")
        game.next_player()
        game.place_piece("a0")
        status = "BAD" if not game.place_piece("a0") else "OK"
        self.assertEqual(status, "BAD")
        self.assertEqual(game.get_game_state(), [['O', '-', '-'], ['-', '-', 'X'], ['-', '-', '-']])

    def test_winner_easy(self):
        """Check the winning condition. In this test, Player 1 (X) will be the winner."""
        # Excluding game.next_player() to simplify the test
        game = TicTacToe()
        # Straight across the top row
        game.place_piece("a0")
        game.place_piece("a1")
        game.place_piece("a2")
        self.assertEqual(game.check_board(), 1)

    def test_winner_normal(self):
        """Check the winning condition. In this test, alternate between Player 1 and 2 normally."""
        game = TicTacToe()
        game.place_piece("a0")
        game.next_player()
        game.place_piece("a1")
        game.next_player()
        game.place_piece("b1")
        game.next_player()
        game.place_piece("a2")
        game.next_player()
        game.place_piece("c2")
        self.assertEqual(game.check_board(), 1)

    def test_no_winner(self):
        """Check the condition in which neither player wins. All spaces have been used up."""
        game = TicTacToe()
        game.board = [["X", "O", "X"], ["X", "O", "O"], ["O", "O", "X"]]
        self.assertEqual(game.check_board(), -1)

# Use only if you are testing directly from running this file.
if __name__ == "__main__":
    unittest.main()

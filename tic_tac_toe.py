"""Module that contains the game logic for a text-based Tic-Tac-Toe"""
class TicTacToe:
    """Creates a TicTacToe object that manages a single instance of a game."""
    def __init__(self) -> None:
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def get_game_state(self):
        """Returns the state of the game board"""
        return self.board
    
"""Module that contains the game logic for a text-based Tic-Tac-Toe"""
class TicTacToe:
    """Creates a TicTacToe object that manages a single instance of a game."""
    def __init__(self) -> None:
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.row_map = {'a': 0, 'b': 1, 'c': 2}
        self.current_player = 1  # Possible values: [1, 2]

    def get_game_state(self):
        """Returns the state of the game board"""
        return self.board

    def display_board(self):
        """Displays the current state of the game board"""
        output = f"""   1     2     3
      |     |     
a  {self.board[0][0]}  |  {self.board[0][1]}  |  {self.board[0][2]}  
 _____|_____|_____
      |     |     
b  {self.board[1][0]}  |  {self.board[1][1]}  |  {self.board[1][2]}  
 _____|_____|_____
      |     |     
c  {self.board[2][0]}  |  {self.board[2][1]}  |  {self.board[2][2]}  
      |     |     """
        print(output)

    def check_board(self):
        """Check the board to see if there are any winning moves."""

    def place_piece(self, location_string):
        """Places an 'X' or 'O' on the board using the format [ROW][COLUMN]. Example: b2"""
        # Do stuff to the game board
        target_row = self.row_map.get(location_string[0])
        target_col = int(location_string[1])
        # TODO: Check to see if the target cell has already been claimed.
        self.board[target_row][target_col] = 'X' if self.current_player == 1 else 'O'

        self.current_player = 1 if self.current_player == 2 else 2
        return self.board

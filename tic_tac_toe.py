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

    def is_valid_move(self, input_string):
        """Validate that the user inputs a {row letter}{column number} for their input string
        and that the move is doable."""
        if (len(input_string) == 2) and (input_string[0] in self.row_map) and (int(input_string[-1]) in self.row_map.values()):
            target = (self.row_map.get(input_string[0]), int(input_string[1]))
            if self.board[target[0]][target[1]] != '-':  # Cell has already been claimed
                return False
            # Cell has not already been claimed
            return True
        
        # Invalid Move
        return False


    def place_piece(self, location_string):
        """Places an 'X' or 'O' on the board using the format {row letter}{column number}.
        Example: b2"""
        # Do stuff to the game board if doable move
        if self.is_valid_move(location_string):
            valid_target = (self.row_map.get(location_string[0]), int(location_string[1]))
            self.board[valid_target[0]][valid_target[1]] = 'X' if self.current_player == 1 else 'O'
            self.current_player = 1 if self.current_player == 2 else 2
            return True

        # TODO: Do something when the move isn't valid.
        return False

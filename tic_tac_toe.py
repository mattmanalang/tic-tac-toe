"""Module that contains the game logic for a text-based Tic-Tac-Toe"""


class TicTacToe:
    """Creates a TicTacToe object that manages a single instance of a game."""
    logo = r"""
    .------------------------------------------------.
    | _____ _        _____            _____          |
    ||_   _(_) ___  |_   _|_ _  ___  |_   _|__   ___ |
    |  | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \|
    |  | | | | (__    | | (_| | (__    | | (_) |  __/|
    |  |_| |_|\___|   |_|\__,_|\___|   |_|\___/ \___||
    '------------------------------------------------'
"""

    def __init__(self) -> None:
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        self.row_map = {"a": 0, "b": 1, "c": 2}
        self.player_map = {1: "X", 2: "O"}
        self.current_player = 1  # Possible values: [1, 2]
        self.game_on = True
        self.moves_made = 0

    def get_game_state(self):
        """Returns the state of the game board"""
        return self.board

    def display_board(self):
        """Displays the current state of the game board"""
        output = f"""   0     1     2
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

    def next_player(self):
        """Set the current player to the next player."""
        self.current_player = 1 if self.current_player == 2 else 2

    def check_board(self):
        """Check the board to see if the current player has made a winning move."""
        target_piece = self.player_map.get(self.current_player)

        # Check patterns that start with the a0 cell
        if self.board[0][0] == target_piece:
            if (
                (self.board[0][0] == self.board[0][1] == self.board[0][2])  # a0 to a2
                or (
                    self.board[0][0] == self.board[1][0] == self.board[2][0]
                )  # a0 to c0
                or (
                    self.board[0][0] == self.board[1][1] == self.board[2][2]
                )  # a0 to c2
            ):
                self.game_on = False
                return self.current_player

        # Check pattern(s) that start with the a1 cell
        if self.board[0][1] == target_piece:
            if self.board[0][1] == self.board[1][1] == self.board[2][1]:  # a1 to c1
                self.game_on = False
                return self.current_player

        # Check pattern(s) that start with the a2 cell
        if self.board[0][2] == target_piece:
            if (self.board[0][2] == self.board[1][2] == self.board[2][2]) or (
                self.board[0][2] == self.board[1][1] == self.board[2][0]
            ):
                self.game_on = False
                return self.current_player

        # Check pattern(s) that start with the b0 cell
        if self.board[1][0] == target_piece:
            if self.board[1][0] == self.board[1][1] == self.board[1][2]:
                self.game_on = False
                return self.current_player

        # Check pattern(s) that start with the c0 cell
        if self.board[2][0] == target_piece:
            if self.board[2][0] == self.board[2][1] == self.board[2][2]:
                self.game_on = False
                return self.current_player

        # All possible spaces have been used up
        if self.moves_made == 9:
            return -999

        # No winning patterns that match
        return -1

    def is_valid_move(self, input_string):
        """Validate that the user inputs a {row letter}{column number} for their input string
        and that the move is doable."""
        if (
            (len(input_string) == 2)
            and (input_string[0] in self.row_map)
            and (int(input_string[-1]) in self.row_map.values())
        ):
            target = (self.row_map.get(input_string[0]), int(input_string[1]))
            if self.board[target[0]][target[1]] != "-":  # Cell has already been claimed
                return False
            # Cell has not already been claimed
            return True

        # Invalid Move
        return False

    def place_piece(self, location_string):
        """Places an 'X' or 'O' on the board using the format {row letter}{column number}.
        Example: b2"""
        target = location_string.lower()

        # Do stuff to the game board if doable move
        if self.is_valid_move(target):
            valid_target = (
                self.row_map.get(target[0]),
                int(target[1]),
            )
            self.board[valid_target[0]][valid_target[1]] = self.player_map.get(
                self.current_player
            )
            self.moves_made += 1
            return True

        return False

    def play(self):
        """Play the game of TicTacToe."""
        # Start game
        print(self.logo)
        print("Player 1 is X, and Player 2 is O")
        input("Press Enter to play...")
        while self.game_on:
            self.display_board()
            player_move = input(f"""Player {self.current_player}: Type in a location to place your {self.player_map.get(self.current_player)}!
Remember: enter a location as [row][column]. Example: a2 or C0\n""")
            if not self.place_piece(player_move):
                print("Could not find that place to put your piece... Please try again.")
                continue
            checkpoint = self.check_board()
            if checkpoint == -1:
                self.next_player()
            elif checkpoint == -999:
                print("No winners!")
                self.game_on = False
            else:
                print(f"Player {checkpoint} wins!")
        self.display_board()
        print("Game Over!")

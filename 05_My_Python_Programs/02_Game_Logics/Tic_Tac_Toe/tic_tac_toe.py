"""
Tic-Tac-Toe Game Engine.

This module provides a fully functional, terminal-based Tic-Tac-Toe game.
It features error-handled user inputs, a dynamic game board, and supports 
both Player vs Player and Player vs Computer modes.

Example:
    Run the script directly to play:
        $ python tic_tac_toe.py
"""

import time
import random

# ==========================================
#              BOARD CLASS
# ==========================================

class Board:
    """
    Represents the Tic-Tac-Toe game board.

    Manages the 3x3 grid, tracks player marks, and checks for 
    win or draw conditions after every turn.

    Attributes:
        x (list of str): A list of 9 strings representing the 9 boxes on the board.
            Empty boxes are represented by a single space (' ').
    """
    def __init__(self):
        """Initializes an empty 3x3 game board."""
        self.x = ['', '', '', '', '', '', '', '', '']


    def __str__(self):
        """
        Formats the board for a clean terminal output.

        Returns:
            str: A visual representation of the 3x3 grid.
        """
        return f"""                   _____________
                   | {self.x[0]} | {self.x[1]} | {self.x[2]} |
                   | {self.x[3]} | {self.x[4]} | {self.x[5]} |
                   | {self.x[6]} | {self.x[7]} | {self.x[8]} |
                   ============="""
    

    def check(self, position, mark):
        """
        Places a mark on the board if the chosen position is empty.

        Args:
            position (int): The chosen box number (1-9).
            mark (str): The player's symbol ('X' or 'O').

        Returns:
            bool: True if the move is valid and placed, False if the box is already full.
        """
        index = int(position) - 1
        if self.x[index] == '':
            self.x[index] = mark
            return True
        else:
            print('\n[!] Position already filled! Please choose another empty box.')
            return False
        
        
    def check_win(self):
        """
        Checks if the current board state contains a winning combination.

        Returns:
            bool: True if a winning pattern is found, False otherwise.
        """
        # All possible winning combinations (Rows, Columns, Diagonals)
        win_combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        
        for a, b, c in win_combos:
            # Check if all 3 boxes match and are not empty
            if self.x[a] == self.x[b] == self.x[c] and self.x[a] != '':
                return True
        return False
        

    def check_draw(self):
        """
        Checks if the game has ended in a draw (all boxes filled).

        Returns:
            bool: True if no empty spaces are left, False otherwise.
        """
        for space in self.x:
            if space == '':
                return False
        return True

# ==========================================
#             PLAYER CLASSES
# ==========================================
     
class Player:
    """
    Represents a human player participating in the game.

    Attributes:
        name (str): The name of the player.
        mark (str): The symbol the player uses on the board.
    """
    def __init__(self):
        """Initializes the human player and asks for name and mark."""
        self.name = input('Enter Your Name: ').title()
        self.mark = input(f'{self.name}, Enter Your Mark (e.g. X or O): ').upper()
    

    def position(self, current_board):
        """
        Prompts the player for their next move with strong error handling.

        Returns:
            int: A validated board position between 1 and 9.
        """
        while True:
            choice = input('Where do you want to make your mark (1-9)? ')
            
            # Error Handling: Checks if input is a number AND between 1-9
            if choice.isdigit() and 1 <= int(choice) <= 9:
                return int(choice)
            else:
                print("[!] Invalid Input! Please enter a number between 1 and 9.")

class Computer:
    """
    Represents an AI/Computer opponent in the game.

    Attributes:
        name (str): The default name ('Computer').
        mark (str): The default mark for the computer ('#').
    """
    def __init__(self):
        """Initializes the computer player with default attributes."""
        self.name = 'Computer'
        self.mark = '#'  


    def position(self, current_board):
        """
        Generates a smart random move by scanning for available empty spots.

        Unlike the human player who might accidentally choose a filled box, the AI 
        first scans the entire board to isolate only the empty indices. It then 
        randomly picks one of these valid indices. This prevents the AI from 
        repeatedly guessing filled spots and spamming the console, especially 
        during the endgame.

        Args:
            board_state (list of str): The current state of the 3x3 game board 
                (list of 9 strings), where empty boxes are represented by ' '.

        Returns:
            int: A randomly chosen, perfectly valid board position between 1 and 9.
        """
        empty_slots = []

        # 1. Iterate over the board array to collect empty square positions
        for index in range(9):
            if current_board[index] == '':
                empty_slots.append(index + 1) # Store 1-based index for the player move
        
        # 2. Select a random position strictly from the list of valid empty spots
        choice = random.choice(empty_slots)
        return choice

# ==========================================
#              GAME LOGIC CLASS
# ==========================================

class Game:
    """
    Core Game Engine for Tic-Tac-Toe.

    Manages the game setup, players, and the main turn-by-turn loop safely 
    without blocking object instantiation.

    Attributes:
        board (Board): The game board instance.
        player1 (Player): The first human player.
        player2 (Player/Computer): The second player or AI.
        current_player (Player/Computer): Tracks whose turn it is.
    """
    def __init__(self):
            """Initializes the board and attributes quietly (no user input)."""
            self.board = Board()
            self.player1 = None
            self.player2 = None
            self.current_player = self.player1


    def setup_game(self):
        """
        Handles game mode selection and player instantiation.
        
        This method safely prompts the user for game settings after the 
        object has been fully constructed.
        """
        print("\n--- Welcome to Tic-Tac-Toe ---")
        mode = input("For User vs User type '1' | For User vs Computer type '2': ")
        
        if mode == '1':
            self.player1 = Player()
            self.player2 = Player()
        else:
            self.player1 = Player()
            self.player2 = Computer()
            
        self.current_player = self.player1


    def play(self):
        """
        Executes the main game loop.

        Handles the initial setup, player turns, board updates, win/draw 
        checking, and switching turns dynamically.
        """
        # Initialize players before starting the loop
        self.setup_game()

        game_over = False

        while game_over == False:
            print(self.board)
            print(f"--- {self.current_player.name}'s turn ---")

            choice = self.current_player.position(self.board.x)

            is_valid_move = self.board.check(choice, self.current_player.mark)
            if is_valid_move == True:

                # Check Win
                if self.board.check_win() == True:
                    print(self.board)
                    print(f'🎉 Congratulations! {self.current_player.name}, you won! 🎉')
                    game_over = True

                # Check Draw
                elif self.board.check_draw() == True:
                    print(self.board)
                    print('🤝 It\'s a Draw! Well played both. 🤝')
                    game_over = True

                # Switch Turns
                else:
                    if self.current_player == self.player1:
                        time.sleep(1)
                        self.current_player = self.player2

                    else:
                        time.sleep(1)
                        self.current_player = self.player1


# ==========================================
#              MAIN EXECUTION
# ==========================================

if __name__ == "__main__":
    my_game = Game()
    my_game.play()
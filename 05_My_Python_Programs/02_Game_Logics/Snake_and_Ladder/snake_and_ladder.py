"""
Snake and Ladder Game Engine.

This module provides a fully functional, terminal-based Snake and Ladder game.
It includes multiple classes to handle different board difficulties (Easy, Medium, Hard),
player types (Human, Computer), and game modes (PvP, PvE).

Example:
    To play the game, simply run this script directly:
        $ python snake_and_ladder.py
"""

from random import randint

# ==========================================
#              BOARD CLASSES
# ==========================================

class EasyBoard:
    """
    Represents the Easy difficulty game board.

    This base class manages the 100-square grid and initializes the locations 
    of snakes and ladders for the easy level. It also handles the visual 
    representation of the board for the terminal.

    Attributes:
        boxs (list of int/str): A list representing the 100 squares on the board.
            Numbers are replaced with 'S' for snakes and 'L' for ladders.
        snake (dict): A dictionary mapping snake head positions (keys) to 
            their tail positions (values).
        ladder (dict): A dictionary mapping ladder bottom positions (keys) to 
            their top positions (values).
    """
    def __init__(self):
        """Initializes the board, setting up standard boxes, snakes, and ladders."""
        self.boxs = [i+1 for i in range(100)]
        self.snake = {27:15, 40:31, 43:20, 54:41, 66:52, 89:71} 
        self.ladder = {4:25, 13:46, 33:49, 42:63, 50:69, 62:81, 74:92}

        # Mark snake heads on the board
        for pos in self.snake:
            index = pos - 1
            self.boxs[index] = 'S'

        # Mark ladder bottoms on the board
        for pos in self.ladder:
            index = pos - 1
            self.boxs[index] = 'L'

    def __str__(self):
        """Formats the board for terminal output.

        Returns:
            str: A formatted string representing the 10x10 game board, 
            with each cell evenly spaced for visual alignment.
        """
        board_view = "\n"
        for i in range(0, 100, 10):
            row = [f"{box:^8}" for box in self.boxs[i:i+10]]
            board_view += "                             |"+"|".join(row) + "|\n"
        return board_view

class MediumBoard(EasyBoard):
    """
    Represents the Medium difficulty game board.

    Inherits from EasyBoard but overrides the snake and ladder placements 
    to increase the difficulty with more hazards.
    """
    def __init__(self):
        """Initializes the medium board with increased snakes and specific ladders."""
        self.boxs = [i+1 for i in range(100)]
        self.snake = {17:4, 34:12, 52:29, 64:36, 73:51, 87:60, 95:75, 98:79}
        self.ladder = {3:22, 8:30, 28:84, 58:77, 75:86, 80:99}

        for pos in self.snake:
            index = pos - 1
            self.boxs[index] = 'S'

        for pos in self.ladder:
            index = pos - 1
            self.boxs[index] = 'L'

    def __str__(self):
        return super().__str__()
    
class HardBoard(EasyBoard):
    """
    Represents the Hard difficulty game board.

    Inherits from EasyBoard but sets up punishing snake placements, 
    especially near the end of the board (e.g., 99 drops to 2).
    """
    def __init__(self):
        """Initializes the hard board with maximum hazards."""
        self.boxs = [i+1 for i in range(100)]
        self.snake = {24:5, 33:9, 48:14, 56:25, 63:18, 72:41, 84:28, 93:50, 97:12, 99:2}
        self.ladder = {2:23, 11:32, 21:42, 36:57, 46:67, 61:79}

        for pos in self.snake:
            index = pos - 1
            self.boxs[index] = 'S'

        for pos in self.ladder:
            index = pos - 1
            self.boxs[index] = 'L'

    def __str__(self):
        return super().__str__()

# ==========================================
#             PLAYER CLASSES
# ==========================================

class Player(): 
    """
    Represents a human player participating in the game.

    Handles the player's identity, their visual marker on the board, 
    and tracks their movement state across turns.

    Args:
        player_mark (str): The symbol used to represent the player on the board (e.g., 'X', 'O').

    Attributes:
        name (str): The customized name inputted by the human player.
        mark (str): The visual marker assigned to the player.
        current_position (int): The current square number the player is on (1-100).
        old_position (int): The previous square number before the latest dice roll.
    """
    def __init__(self, player_mark):
        """Initializes a new human player and prompts for their name."""
        self.name = input('Enter Your Name: ').title()
        self.mark = player_mark
        self.current_position = 0
        self.old_position = 0

    def dice_roll(self):
        """Simulates a dice roll and calculates the new potential position.

        The method prompts the user to roll, generates a random number between 1-6,
        and checks if the resulting move is valid (does not exceed box 100).

        Returns:
            bool: True if the move is valid and position updated, False if the 
            roll causes the player to exceed 100 (turn skipped).
        """
        self.ask = input(f'{self.name}, input anything to roll the dice: ')
        self.dice = randint(1, 6)
        print(f"{self.name}, your dice result is: {self.dice}")
        if self.current_position + self.dice <= 100:
            self.old_position = self.current_position
            self.current_position = self.current_position + self.dice
            return True 
        else:
            return False 
        
class Computer(Player):
    """
    Represents an AI/Computer player.

    Inherits from the Player class but overrides initialization and dice rolling 
    methods to function automatically without requiring manual user input.

    Args:
        player_mark (str): The symbol used to represent the computer (e.g., 'O').
    """
    def __init__(self, player_mark):
        """Initializes the computer player with a default name."""
        self.name = 'Computer'
        self.mark = player_mark
        self.current_position = 0
        self.old_position = 0

    def dice_roll(self):
        """Automatically rolls the dice for the computer.

        Returns:
            bool: True if the move is valid, False if it exceeds 100.
        """
        self.dice = randint(1, 6)
        print(f"{self.name}'s dice result is: {self.dice}")
        if self.current_position + self.dice <= 100:
            self.old_position = self.current_position
            self.current_position = self.current_position + self.dice
            return True
        else:
            return False

# ==========================================
#              GAME LOGIC CLASSES
# ==========================================

class EasyUserGame():
    """Core Game Engine for Easy Difficulty (Player vs Player).

    This class manages the main game loop, player turns, board state updates, 
    and checks for snakes, ladders, and win conditions. Other game modes 
    inherit this logic to avoid code duplication.

    Attributes:
        board (EasyBoard): The initialized game board object.
        player1 (Player): The first human player (X).
        player2 (Player): The second human player (O).
        current_player (Player): Tracks whose turn it is currently.
    """
    def __init__(self):
        """Initializes the game board and the two participating players."""
        self.board = EasyBoard()
        self.player1 = Player(' "X"')
        self.player2 = Player(' "O"') 
        self.current_player = self.player1

    def game_play(self):
        """
        Executes the main turn-by-turn game loop.

        This method handles:
        1. Dice rolling.
        2. Cleaning up the player's previous board position.
        3. Handling overlaps (if two players land on the same square).
        4. Triggering snakes (falling) or ladders (climbing).
        5. Updating the board with the new position.
        6. Checking if a player has reached 100 (win condition).
        """
        game_over = False
        while game_over == False:
            print(self.board)
            print(f"--- {self.current_player.name}'s turn ---")

            dice_roll_result = self.current_player.dice_roll()

            if dice_roll_result == True:
                # Identify the opponent to handle overlapping positions
                if self.current_player == self.player1:
                    other_player = self.player2
                else:
                    other_player = self.player1

                # Clean up the old position
                if self.current_player.old_position > 0:
                    old_index = self.current_player.old_position - 1

                    # If the opponent is on the old spot, leave their mark
                    if other_player.current_position == self.current_player.old_position:
                        self.board.boxs[old_index] = other_player.mark
                    else:
                        # Otherwise, restore the original square number/symbol
                        self.board.boxs[old_index] = old_index + 1

                # Check for Snakes or Ladders interactions
                current_pos = self.current_player.current_position 
                if current_pos in self.board.snake:
                    print(f"Oh no! A snake bit {self.current_player.name}. Sliding down to {self.board.snake[current_pos]}.")
                    self.current_player.current_position = self.board.snake[current_pos]

                elif current_pos in self.board.ladder:
                    print(f"Yay! {self.current_player.name} found a ladder. Climbing to {self.board.ladder[current_pos]}.")
                    self.current_player.current_position = self.board.ladder[current_pos]

                # Update the new position on the board
                new_index = self.current_player.current_position - 1

                # Combine marks if both players share the same square
                if other_player.current_position == self.current_player.current_position:
                    self.board.boxs[new_index] = self.current_player.mark + other_player.mark

                else:
                    self.board.boxs[new_index] = self.current_player.mark 

            # Win Condition Check
            if self.current_player.current_position == 100:
                print(self.board)
                print(f"🎉 Congratulations, {self.current_player.name}! You won the game! 🎉")
                game_over = True
                break
            
            # Switch Turns
            if self.current_player == self.player1:
                self.current_player = self.player2

            else:
                self.current_player = self.player1

class MediumUserGame(EasyUserGame):
    """Medium Difficulty (Player vs Player). Overrides board initialization."""
    def __init__(self):
        self.board = MediumBoard()
        self.player1 = Player(' "X"')
        self.player2 = Player(' "O"')
        self.current_player = self.player1

    def __str__(self):
        return super().__str__()
    
class HardUserGame(EasyUserGame):
    """Hard Difficulty (Player vs Player). Overrides board initialization."""
    def __init__(self):
        self.board = HardBoard()
        self.player1 = Player(' "X"')
        self.player2 = Player(' "O"')
        self.current_player = self.player1

    def __str__(self):
        return super().__str__()

class EasyComputerGame(EasyUserGame):
    """Easy Difficulty (Player vs Computer). Injects Computer class for player 2."""
    def __init__(self):
        self.board = EasyBoard()
        self.player1 = Player(' "X"')
        self.player2 = Computer(' "O"')
        self.current_player = self.player1

    def game_play(self):
        return super().game_play()
    
class MediumComputerGame(EasyUserGame):
    """Medium Difficulty (Player vs Computer)."""
    def __init__(self):
        self.board = MediumBoard()
        self.player1 = Player(' "X"') 
        self.player2 = Computer(' "O"') 
        self.current_player = self.player1

    def game_play(self):
        return super().game_play()
    
class HardComputerGame(EasyUserGame):
    """Hard Difficulty (Player vs Computer)."""
    def __init__(self):
        self.board = HardBoard()
        self.player1 = Player(' "X"')
        self.player2 = Computer(' "O"') 
        self.current_player = self.player1

    def game_play(self):
        return super().game_play()


# ==========================================
#              MAIN EXECUTION
# ==========================================

if __name__ == "__main__":
    while True:
        play = input("\nEnter '1' to start the game or '2' to exit: ")
        
        if play == '1':
            print("\n--- Choose your Mode and Difficulty Level ---")
            user_mode = input("For User vs User type '1' | For User vs Computer type '2': ")
            user_level = input("Enter '1' for Easy | '2' for Medium | '3' for Hard: ")
            
            if user_mode == '1' and user_level == '1':
                game = EasyUserGame()
                game.game_play()
            elif user_mode == '1' and user_level == '2':
                game = MediumUserGame()
                game.game_play()
            elif user_mode == '1' and user_level == '3':
                game = HardUserGame()
                game.game_play()
            elif user_mode == '2' and user_level == '1':
                game = EasyComputerGame()
                game.game_play()
            elif user_mode == '2' and user_level == '2':
                game = MediumComputerGame()
                game.game_play()
            elif user_mode == '2' and user_level == '3':
                game = HardComputerGame()
                game.game_play()
            else:
                print("Invalid mode or level selected. Try again.")
                continue
                
        elif play == '2':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print('Wrong Input! Please choose 1 or 2.')
            continue
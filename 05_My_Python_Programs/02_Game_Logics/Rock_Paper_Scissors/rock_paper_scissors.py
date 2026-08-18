"""
Rock, Paper, Scissors Game

This script allows a user to play a classic game of Rock, Paper, Scissors 
against the computer. It keeps track of the score over a series of rounds 
and declares the final winner.

Author: Lokendra Kushwaha
"""

import random
import datetime

def play_rock_paper_scissors(total_chances: int = 5) -> None:
    """
    Executes the main game loop for Rock, Paper, Scissors.
    
    Args:
        total_chances (int): The total number of rounds the user is allowed to play. 
                             Defaults to 5.
        
    Returns:
        None
    """
    user_score = 0
    computer_score = 0
    rounds_played = 0
    chances_left = total_chances
    
    # Dictionary to define winning rules (Key beats Value)
    rules = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
    
    # Dictionary to handle abbreviations and standardize inputs
    shortcuts = {
        'R': 'Rock', 'P': 'Paper', 'S': 'Scissors',
        'Rock': 'Rock', 'Paper': 'Paper', 'Scissors': 'Scissors'
    }

    print("=" * 80)
    print("Welcome to Rock, Paper, Scissors!")
    print("=" * 80)

    # A while loop is here so invalid inputs don't consume a chance
    while chances_left > 0:
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        
        # Taking and normalizing user input
        user_input = input(
            "Enter Rock, Paper or Scissors (or R/P/S). Type 'Exit' to quit: "
        ).capitalize()
        
        if user_input == "Exit":
            print("\nExiting the game. Thanks for playing!")
            break

        # Handle invalid inputs
        if user_input not in shortcuts:
            print("-> Invalid Input! Please choose a valid option.\n")
            continue  # Skips to the next iteration without reducing chances_left

        # Standardize the user's choice
        user_choice = shortcuts[user_input]
        rounds_played += 1
        chances_left -= 1  # Reduce the chance only on a valid turn
        
        print('-' * 80)
        print(f"Round {rounds_played} | Your Choice: {user_choice}  vs  My Choice: {computer_choice}")

        # Determine the winner of the round
        if user_choice == computer_choice:
            print("Result: Round is Tied!")
            
        elif rules[user_choice] == computer_choice:
            print("Result: Hurrah! You Won this round!")
            user_score += 1
            
        else:
            print("Result: Oh no! I (Computer) Won this round!")
            computer_score += 1

        print(f"Chances left: {chances_left}")
        print('-' * 80 + "\n")

    # Final Score Display
    print("=" * 80)
    print("GAME OVER - FINAL RESULTS")
    print("=" * 80)
    print(f"Your Total Score   -> {user_score}")
    print(f"My Total Score     -> {computer_score}")
    print("-" * 80)

    # Declare the overall winner
    if computer_score > user_score:
        final_result = "Computer Won"
        print("Final Result: You Lose 😓 Better luck next time!")
    elif computer_score == user_score:
        final_result = "Match Tied"
        print("Final Result: Match Tied 😎 Well played!")
    else:
        final_result = "User Won"
        print("Final Result: Congratulations! You Won 🎉")
    print("=" * 80)


    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] User Score: {user_score} | Computer Score: {computer_score} | Result: {final_result}\n"
    
    with open("score_history.txt", "a") as file:
        file.write(log_entry)
        
    print("-> Your match result has been securely saved to 'score_history.txt'!")
    print("=" * 80)


if __name__ == "__main__":
    # Entry point of the script
    play_rock_paper_scissors(total_chances=5)
"""
Number Guessing Game.

This module provides a simple, terminal-based number guessing game. 
The system generates a random jackpot number between 1 and 100, and 
guides the user with "higher" or "lower" hints until they guess it correctly.

Example:
    Run the script directly from the terminal to play:
        $ python guessing_game.py
"""

import random

def play_guessing_game():
    """
    Executes the core game loop for the Number Guessing Game.

    Generates a random integer between 1 and 100. It continuously prompts 
    the user for a guess, validates the input to prevent crashes, provides 
    directional feedback (higher/lower), and tracks the total number of attempts.
    """
    print("-" * 50)
    print("🎮 Welcome to the Number Guessing Game! 🎮")
    print("I have chosen a random number between 1 and 100.")
    print("-" * 50)

    # Generate the random jackpot number
    jackpot = random.randint(1, 100)
    counter = 0

    # Start the infinite game loop
    while True:
        try:
            # Prompt user for input and convert it to an integer
            guess = int(input("\nEnter your guess: "))
            counter += 1  # Increment the attempt counter

            # Logic to check the guess against the jackpot
            if guess < jackpot:
                print("❌ Wrong! Guess HIGHER ⬆️")
            elif guess > jackpot:
                print("❌ Wrong! Guess LOWER ⬇️")
            else:
                # If the guess is exactly equal to the jackpot
                print("\n🎉 CORRECT GUESS! 🎉")
                print(f"Awesome! You found the jackpot in {counter} attempts.")
                print("-" * 50)
                break  # Exit the game loop
                
        except ValueError:
            # Error handling: If the user types a string/letter instead of a number
            print("[!] Invalid input! Please enter a valid whole number.")

# ==========================================
#              MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    play_guessing_game()
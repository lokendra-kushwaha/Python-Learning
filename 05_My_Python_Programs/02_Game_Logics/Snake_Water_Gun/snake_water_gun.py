"""
Snake - Water - Gun Game

A Python logic game played against the computer.
Rules:
- Snake drinks Water
- Water rusts Gun
- Gun shoots Snake

Created By: Lokendra Kushwaha
"""

import random

def play_snake_water_gun():
    total_chances = 5
    user_score = 0
    computer_score = 0
    
    # Advanced Logic: Key defeats Value
    rules = {'Water': 'Gun', 'Gun': 'Snake', 'Snake': 'Water'}
    valid_choices = ['Snake', 'Water', 'Gun']

    print("🐍💧🔫 Welcome to Snake - Water - Gun! 🐍💧🔫")
    print("You have 5 rounds to beat the computer. Good luck!\n")

    for round_num in range(1, total_chances + 1):
        # Input Validation Loop: Prevents KeyError if user types wrong spelling
        while True:
            user_choice = input(f"Round {round_num} - Enter Choice (Snake/Water/Gun): ").title().strip()
            if user_choice in valid_choices:
                break
            print("Invalid spelling! Please type exactly Snake, Water, or Gun.\n")

        computer_choice = random.choice(valid_choices)
        print(f"\nYour Choice: {user_choice}   |   Computer's Choice: {computer_choice}")

        # The Core Game Logic
        if user_choice == computer_choice:
            print('Result: It\'s a Draw! 🤝\n')
        elif rules[user_choice] == computer_choice:
            print('Result: You Won this round! 🎉\n')
            user_score += 1
        else:
            print('Result: You Lost this round! 😓\n')
            computer_score += 1

        print(f"Chances left: {total_chances - round_num}")
        print("=" * 60)

    # Final Scoreboard
    print(f"\nFINAL SCOREBOARD")
    print(f"Your Score: {user_score}   |   Computer Score: {computer_score}")

    if computer_score > user_score:
        print("Verdict: The Computer Won! Better luck next time. 😓")
    elif computer_score == user_score:
        print("Verdict: Match Tied! It's a tough battle. 😎")
    else:
        print("Verdict: Congratulations! You Won the Game! 🏆")
    print("=" * 60)

if __name__ == "__main__":
    play_snake_water_gun()
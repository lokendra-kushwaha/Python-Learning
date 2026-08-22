"""
=========================================================
🏆 RPS EVOLUTION: VERSION 3 (COMPOUND CONDITIONS) 🏆
=========================================================

Description:
    In this version, I abandoned the complex array slicing and moved to 
    standard logical operators (`in`, `and`). 
    
    This script evaluates the game using direct compound conditional 
    statements (e.g., `if user == X and comp == Y`). It also handles 
    user input flexibility by allowing both full words ('Rock') and 
    single letters ('R'). 
    
    This is the closest stepping stone to the final, highly optimized 
    mathematical version (0, 1, 2 mapping) I wrote later on.

Created By: Lokendra Kushwaha
"""

import random

user_chance = 5
user_score = 0
computer_score = 0

for i in range(5):
    user_chance = user_chance - 1
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    user_choice = input("Enter Rock, Paper or Scissors (or R/P/S) or \"Exit\": ").capitalize()
    
    print("="*80)
    print(f"Your Choice: {user_choice}       My Choice: {computer_choice}")

    # Evaluating using standard logical conditions
    if user_choice in ['Rock', 'R'] and computer_choice in ['Rock']:
        print(f"{i+1} - Round is Tied")
    elif user_choice in ['Paper', 'P'] and computer_choice in ['Paper']:
        print(f"{i+1} - Round is Tied")
    elif user_choice in ['Scissor', 'S'] and computer_choice in ['Scissors']:
        print(f"{i+1} - Round is Tied")
    elif user_choice in ['Rock', 'R'] and computer_choice in ['Paper']:
        print(f"{i+1} - Oh no! I Lose 😓")
        computer_score = computer_score + 1
    elif user_choice in ['Scissors', 'S'] and computer_choice in ['Rock']:
        print(f"{i+1} - Oh no! I Lose 😓")
        computer_score = computer_score + 1
    elif user_choice in ['Paper', 'P'] and computer_choice in ['Scissors']:
        print(f"{i+1} - Oh no! I Lose 😓")
        computer_score = computer_score + 1
    elif user_choice in ['Scissors', 'S'] and computer_choice in ['Paper']:
        print(f"{i+1} - Hurrah! I Won 😎")
        user_score = user_score + 1
    elif user_choice in ['Paper', 'P'] and computer_choice in ['Rock']:
        print(f"{i+1} - Hurrah! I Won 😎")
        user_score = user_score + 1
    elif user_choice in ['Rock', 'R'] and computer_choice in ['Scissors']:
        print(f"{i+1} - Hurrah! I Won 😎")
        user_score = user_score + 1
    else:
        print("Enter a Valid Input!")
        
    print(f"You have left only {user_chance} Chances")
    print("="*80)

print(f"Your Total Score → {user_score}         My Total Score → {computer_score}")

if computer_score > user_score:
    print("You Lose 😓")
elif computer_score == user_score:
    print("Match Tied 😎")
else:
    print("Congratulation! You Won 🎉")
print("="*80)
"""
=========================================================
🏆 RPS EVOLUTION: VERSION 2 (PATTERN ARRAY APPROACH) 🏆
=========================================================

Description:
    This marks a huge leap from the V1 (Hardcoded) version. Here, I 
    finally introduced the 'random' module to make the computer's moves 
    unpredictable.
    
    The most unique feature of this code is how wins/losses are calculated. 
    Instead of standard conditions, I created a 2D list (`possible_patterns`) 
    containing all 9 possible match outcomes. I then sliced the array [0:2] 
    to match the [user_choice, computer_choice] combination. 
    
    This is raw, creative data-structuring before I learned Dictionaries!

Created By: Lokendra Kushwaha
"""

import random

user_chance = 5
user_score = 0
computer_score = 0

for i in range(5):
    user_chance = user_chance - 1
    
    # The Creative 2D Array Pattern Logic
    possible_patterns = [
        ['Rock', 'Rock', 'Tied'], ['Rock', 'Paper', 'Loose'], ['Rock', 'Scissors', 'Won'], 
        ['Paper', 'Rock', 'Won'], ['Paper', 'Paper', 'Tied'], ['Paper', 'Scissors', 'Loose'], 
        ['Scissors', 'Rock', 'Loose'], ['Scissors', 'Paper', 'Won'], ['Scissors', 'Scissors', 'Tied']
    ]
    
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    user_choice = input("Enter Rock, Paper or Scissors or for Exit type \"Exit\": ").capitalize()
    
    print("="*80)
    print(f"Your Choice: {user_choice}       My Choice: {computer_choice}")

    random_pattern = [user_choice, computer_choice]

    # Matching the generated pattern with the master array
    if possible_patterns[0][0:2] == random_pattern:
        print(f"{i+1}- Round: {possible_patterns[0][2]}")
    elif possible_patterns[1][0:2] == random_pattern:
        print(f"{i+1} - Round: {possible_patterns[1][2]}")
        computer_score = computer_score + 1
    elif possible_patterns[2][0:2] == random_pattern:
        print(f"{i+1} - Round: {possible_patterns[2][2]}")
        user_score = user_score + 1
    elif possible_patterns[3][0:2] == random_pattern:
        print(f"{i+1} - Round: {possible_patterns[3][2]}")
        user_score = user_score + 1
    elif possible_patterns[4][0:2] == random_pattern:
        print(f"{i+1} - Round: {possible_patterns[4][2]}")
    elif possible_patterns[5][0:2] == random_pattern:
        print(f"{i+1} - Round: {possible_patterns[5][2]}")
        computer_score = computer_score + 1
    elif possible_patterns[6][0:2] == random_pattern:
        print(f"{i+1} - Round: {possible_patterns[6][2]}")
        computer_score = computer_score + 1
    elif possible_patterns[7][0:2] == random_pattern:
        print(f"{i+1} - Round: {possible_patterns[7][2]}")
        user_score = user_score + 1
    elif possible_patterns[8][0:2] == random_pattern:
        print(f"{i+1} - Round: {possible_patterns[8][2]}")
    else:
        print("Wrong Input!")

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
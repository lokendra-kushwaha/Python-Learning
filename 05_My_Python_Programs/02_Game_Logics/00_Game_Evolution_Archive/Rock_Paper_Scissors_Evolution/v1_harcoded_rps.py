"""
=========================================================
🏆 HARDCODED GAME: VERSION 1 ROCK, PAPER, SCISSORS 🏆
=========================================================

Description:
    This is one of my earliest game implementations. Instead of using 
    the 'random' module to make the computer unpredictable, I hardcoded 
    all 5 of the computer's choices in advance! 
    
    It also features manual evaluation of all 5 rounds without using 
    a single conditional loop for checking. A true brute-force classic.

Key Features of my early coding style:
    - Heavy use of print formatting (====) for a console UI.
    - Using time.sleep() to create dramatic suspense.
    - Fully hardcoded logic.

Created By: Lokendra Kushwaha
"""

import time 

print("\n"+"="*110)
print("                     Rock, Paper, Scissors Shoot Computer Game.🤖")
print("="*110)

user_turns = 5 
user_choices = [] 
user_score = 0 
computer_score = 0 

# Taking user inputs for all 5 rounds first
for i in range(5):
        turns_left = user_turns - (i+1)
        print("\n")
        print("First Your Turn🙍 →")
        print("-"*110)
        user_choice = input("Enter Rock, Paper or Scissors (or R/P/S) or 'Exit': ").capitalize() 
        user_choices.append(user_choice) 

        if user_choice == "Rock" or user_choice == "R":
            print("You Choose", '"', user_choice.capitalize(), '"', "🪨 ", "(", "You have left only", turns_left, "turn", ")")
        elif user_choice == "Paper" or user_choice == "P":
            print("You Choose", '"', user_choice.capitalize(), '"', "📃 ", "(", "You have left only", turns_left, "turn", ")")
        elif user_choice == "Scissors" or user_choice == "S":
            print("You Choose", '"', user_choice.capitalize(), '"', "✂️ ", "(", "You have left only", turns_left, "turn", ")")
        elif user_choice == "Exit": 
            break
        else:
            print("Please Write Correct Input.") 
            break

# The "Hardcoded" Computer Moves
print("\n"+"="*80)      
print("Now My Turn🤖 →")
print("-"*80)
time.sleep(1)

print("1. Rock") 
time.sleep(1)
print("2. Scissors")
time.sleep(1)
print("3. Rock")
time.sleep(1)
print("4. Paper")
time.sleep(1)
print("5. Scissors")
time.sleep(1)
            
# Printing Final Result round by round
print("\n"+"="*80)           
print("Final Result🤯 →")
time.sleep(1)

# Compare Round 1
print("-"*80)
print("My First Turn → Rock     ", "                 Your First Turn → ", user_choices[0])
if user_choices[0] == "Rock" or user_choices[0] == "R":
    print("First Round is Tied")
elif user_choices[0] == "Paper" or user_choices[0] == "P":
    print("Oh no! I Lose 😓")
    user_score += 1
elif user_choices[0] == "Scissors" or user_choices[0] == "S":
    print("Hurrah! I Won 😎")
    computer_score += 1

# Compare Round 2
print("-"*80)
print("My Second Turn → Scissors", "                 Your Second Turn → ", user_choices[1])
if user_choices[1] == "Scissors" or user_choices[1] == "S":
    print("Second Round is Tied")
elif user_choices[1] == "Rock" or user_choices[1] == "R":
    print("Oh no! I Lose 😓")
    user_score += 1
elif user_choices[1] == "Paper" or user_choices[1] == "P":
    print("Hurrah! I Won 😎")
    computer_score += 1

# Compare Round 3
print("-"*80)
print("My Third Turn → Rock     ", "                 Your Third Turn → ", user_choices[2])
if user_choices[2] == "Rock" or user_choices[2] == "R":
    print("Third Round is Tied")
elif user_choices[2] == "Paper" or user_choices[2] == "P":
    print("Oh no! I Lose 😓")
    user_score += 1
elif user_choices[2] == "Scissors" or user_choices[2] == "S":
    print("Hurrah! I Won 😎")
    computer_score += 1

# Compare Round 4
print("-"*80)
print("My Forth Turn → Paper   ", "                  Your Forth Turn → ", user_choices[3])
if user_choices[3] == "Paper" or user_choices[3] == "P":
    print("Forth Round is Tied")
elif user_choices[3] == "Rock" or user_choices[3] == "R":
    print("Hurrah! I Won 😎")
    computer_score += 1
elif user_choices[3] == "Scissors" or user_choices[3] == "S":
    print("Oh no! I Lose 😓")
    user_score += 1

# Compare Round 5
print("-"*80)
print("My Fivth Turn → Scissors ", "                 Your Fivth Turn → ", user_choices[4])
if user_choices[4] == "Scissors" or user_choices[4] == "S":
    print("First Round is Tied")
elif user_choices[4] == "Rock" or user_choices[4] == "R":
    print("Oh no! I Lose 😓")
    user_score += 1
elif user_choices[4] == "Paper" or user_choices[4] == "P":
    print("Hurrah! I Won 😎")
    computer_score += 1
    
# Printing Final Score card
print("\n" + "="*80) 
print("Score Card 📜 →")
print("="*80)

match user_choices[0]:
    case "Rock" | "R": print("First Round.  →  My Score : 0            Your Score : 0")
    case "Paper" | "P": print("First Round.  →  My Score : 0            Your Score : 1")
    case "Scissors" | "S": print("First Round.  →  My Score : 1            Your Score : 0")

match user_choices[1]:
    case "Rock" | "R": print("Second Round. →  My Score : 0            Your Score : 1")
    case "Paper" | "P": print("Second Round. →  My Score : 1            Your Score : 0")
    case "Scissors" | "S": print("Second Round. →  My Score : 0            Your Score : 0")

match user_choices[2]:
    case "Rock" | "R": print("Third Round.  →  My Score : 0            Your Score : 0")
    case "Paper" | "P": print("Third Round.  →  My Score : 0            Your Score : 1")
    case "Scissors" | "S": print("Third Round.  →  My Score : 1            Your Score : 0")

match user_choices[3]:
    case "Rock" | "R": print("Forth Round.  →  My Score : 1            Your Score : 0")
    case "Paper" | "P": print("Forth Round.  →  My Score : 0            Your Score : 0")
    case "Scissors" | "S": print("Forth Round.  →  My Score : 0            Your Score : 1")

match user_choices[4]:
    case "Rock" | "R": print("Fivth Round.  →  My Score : 0            Your Score : 1")
    case "Paper" | "P": print("Fivth Round.  →  My Score : 1            Your Score : 0")
    case "Scissors" | "S": print("Fivth Round.  →  My Score : 0            Your Score : 0")

print("="*80)
print("                 My Total Score →", computer_score, "     Your Total Score →", user_score)
print("-"*80)

if computer_score > user_score:
    print("You Lose 😓")
elif computer_score == user_score:
    print("Match Tied 😎")
else:
    print("Congratulation! You Won 🎉")

print("="*80)
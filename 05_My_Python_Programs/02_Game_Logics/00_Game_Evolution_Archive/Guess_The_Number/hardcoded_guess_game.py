"""
=========================================================
🏆      GAME: HARDCODED GUESS THE NUMBER 🏆
=========================================================

Description:
    An early iteration of a "Guess the Number" game. 
    Instead of using the 'random' module to generate a mystery 
    number, the winning number is strictly hardcoded to '53'! 

Fun Developer Quirks in this Code:
    1. Brute-forced Logic: The exact same core logic is copy-pasted 
       three times for Easy, Medium, and Hard levels.
    2. Hidden Pythonic Genius: Despite the hardcoded brute-force, 
       the code uses advanced Python features like chained comparisons 
       (35 <= guess <= 52) and the rare 'for-else' construct!

Created By: Lokendra Kushwaha
"""

print("In this game, you have how many chances according to game level. If you guess the number in given chances, you will win vice versa loose.")
print("Choose the game level. \n1. Easy        2. Medium       3. Hard")

user = input("Please Type Your Name :").capitalize() 
x = input("Enter Level (Easy/Medium/Hard): ").title() 

# Easy level if user choose.
if x == "Easy":
    total_chances = 10
    for i in range(10): 
        guess = int(input("Enter a Random Number: ")) 
        chances_left = total_chances - (i + 1)

        if guess >= 70: 
            print("Oh!", user , ",", "This Number is Too High. 🫣 ", "(" , "Chances Left:", chances_left, ")")
        elif 35 <= guess <= 52: 
            print("Oh!", user, ",", "You are very Close.😲🤦‍♀️ ", "(" , "Chances Left:", chances_left, ")")
        elif 54 <= guess < 70: 
            print("Oh!", user, ",", "You are very Close.😲🤦‍♀️ ", "(" , "Chances Left:", chances_left, ")")
        elif guess < 35: 
            print("Oh!", user, ",", "This Number is Too Low. 🫣 ", "(" , "Chances Left:", chances_left, ")")

        if guess == 53: 
            print("Congratulation!", user,"You Win, Random No. is 53 .👌🫡")
            break 
    else:
         print("Ops!", user,"You Lose.😓") 

# Medium level if user choose.
if x == "Medium":
    total_chances = 5 
    for i in range(5):
        guess = int(input("Enter a Random Number: ")) 
        chances_left = total_chances - (i + 1)

        if guess >= 70: 
            print("Oh!", user, ",", "This Number is Too High. 🫣 " , "(" , "Chances Left:", chances_left, ")")
        elif 35 <= guess <= 52: 
            print("Oh!", user, ",", "You are very Close.😲🤦‍♀️ ", "(" , "Chances Left:", chances_left, ")")
        elif 54 <= guess < 70: 
            print("Oh!", user, ",", "You are very Close.😲🤦‍♀️ ", "(" , "Chances Left:", chances_left, ")")
        elif guess < 35: 
            print("Oh!", user, ",", "This Number is Too Low. 🫣 ", "(" , "Chances Left:", chances_left, ")")

        elif guess == 53: 
            print("Congratulation!", user, "You Win, Random No. is 53 .👌🫡")
            break 
    else:
         print("Ops!", user,"You Lose.😓") 

# Hard level if user choose.
if x == "Hard":
    total_chances = 3
    for i in range(3):
        guess = int(input("Enter a Random Number: ")) 
        chances_left = total_chances - (i + 1)

        if guess >= 70: 
            print("Oh!", user, ",", "This Number is Too High. 🫣 " , "(" ,"Chances Left:", chances_left, ")")
        elif 35 <= guess <= 52: 
            print("Oh!", user, ",", "You are very Close.😲🤦‍♀️ " , "(" , "Chances Left:", chances_left, ")")
        elif 54 <= guess < 70: 
            print("Oh!", user, ",", "You are very Close.😲🤦‍♀️ " , "(" , "Chances Left:", chances_left, ")")
        elif guess < 35: 
            print("Oh!", user, ",", "This Number is Too Low. 🫣 " , "(" , "Chances Left:", chances_left, ")")

        elif guess == 53: 
            print("Congratulation!", user, "You Win, Random No. is 53 .👌🫡")  
            break 
    else:
         print("Ops!", user,"You Lose.😓")
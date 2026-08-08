print("In this game, you have how many chances according to game level. If you guess the number in given chances, you will win vice versa loose.")

print("Choose the game level. \n1. Easy        2. Medium       3. Hard")

user = input("Please Type Your Name :").capitalize() # User Name
x = input("Enter Level (Easy/Medium/Hard): ").title() # Choose a Level 

# Easy level if user choose.
if x == "Easy":

    total_chances = 10
    for i in range(10): # 10 Chances 
        guess = int(input("Enter a Random Number: ")) # Input for random number by user
        chances_left = total_chances - (i + 1)

        if guess >= 70: # if user enter a number greater than 70
            print("Oh!", user , ",", "This Number is Too High. 🫣 ", "(" , "Chances Left:", chances_left, ")")

        elif 35 <= guess <= 52: # if user enter a number between 35-52
            print("Oh!", user, ",", "You are very Close.😲🤦‍♀️ ", "(" , "Chances Left:", chances_left, ")")
            
        elif 54 <= guess < 70: # if user enter a number between 54-70
            print("Oh!", user, ",", "You are very Close.😲🤦‍♀️ ", "(" , "Chances Left:", chances_left, ")")

        elif guess < 35: # if user enter a number less than 35
                print("Oh!", user, ",", "This Number is Too Low. 🫣 ", "(" , "Chances Left:", chances_left, ")")

        if guess == 53: # if user enter a number 53
            print("Congratulation!", user,"You Win, Random No. is 53 .👌🫡")
            break # if user guess number than break the loop
    else:
         print("Ops!", user,"You Lose.😓") # if user can'nt quess number

# Medium level if user choose.
if x == "Medium":

    total_chances = 5 # 5 Chances 
    for i in range(5):
        guess = int(input("Enter a Random Number: ")) # Input for random number by user
        chances_left = total_chances - (i + 1)

        if guess >= 70: # if user enter a number greater than 70
            print("Oh!", user, ",", "This Number is Too High. 🫣 " , "(" , "Chances Left:", chances_left, ")")

        elif 35 <= guess <= 52: # if user enter a number between 35-52
            print("Oh!", user, ",", "You are very Close.😲🤦‍♀️ ", "(" , "Chances Left:", chances_left, ")")
            
        elif 54 <= guess < 70: # if user enter a number between 54-70
            print("Oh!", user, ",", "You are very Close.😲🤦‍♀️ ", "(" , "Chances Left:", chances_left, ")")

        elif guess < 35: # if user enter a number less than 35
                print("Oh!", user, ",", "This Number is Too Low. 🫣 ", "(" , "Chances Left:", chances_left, ")")

        elif guess == 53: # if user enter a number 53
            print("Congratulation!", user, "You Win, Random No. is 53 .👌🫡")
            break # if user guess number than break the loop
    else:
         print("Ops!", user,"You Lose.😓") # if user can'nt quess number

# Hard level if user choose.
if x == "Hard":

    total_chances = 3
    for i in range(3):
        guess = int(input("Enter a Random Number: ")) # Input for random number by user
        chances_left = total_chances - (i + 1)

        if guess >= 70: # if user enter a number greater than 70
            print("Oh!", user, ",", "This Number is Too High. 🫣 " , "(" ,"Chances Left:", chances_left, ")")

        elif 35 <= guess <= 52: # if user enter a number between 35-52
            print("Oh!", user, ",", "You are very Close.😲🤦‍♀️ " , "(" , "Chances Left:", chances_left, ")")
            
        elif 54 <= guess < 70: # if user enter a number between 54-70
            print("Oh!", user, ",", "You are very Close.😲🤦‍♀️ " , "(" , "Chances Left:", chances_left, ")")

        elif guess < 35: # if user enter a number less than 35
                print("Oh!", user, ",", "This Number is Too Low. 🫣 " , "(" , "Chances Left:", chances_left, ")")

        elif guess == 53: # if user enter a number 53
            print("Congratulation!", user, "You Win, Random No. is 53 .👌🫡")  
            break # if user guess number than break the loop
    
    else:
         print("Ops!", user,"You Lose.😓") # if user cann't quess number                
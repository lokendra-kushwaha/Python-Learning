"""
=========================================================
🏆 MY VERY FIRST PYTHON SCRIPTS (PRE-LOOP ERA) 🏆
=========================================================

Description:
    This file contains my earliest attempts at building a CLI calculator.
    It serves as a time capsule from the days before I knew about 'for' 
    or 'while' loops. It showcases pure logical brute-forcing to keep 
    the program running!

Versions Included:
    1. The If-Else Approach (Commented out)
    2. The Match-Case Approach (Python 3.10+)

Created By: Lokendra Kushwaha
"""

# =====================================================================
# VERSION 1: The Basic If-Else Approach 
# =====================================================================

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# Addition of Two Numbers
addCondition = input("For Addition Press 1 : ")

if(addCondition == "1"):
    print("First Number + Second Number = ", num1 + num2)
else:
    print("Please Enter 1")
    print(input("Enter - 1 : "))
    if(print(input("Enter - 1 : ")) == "1"):
        print("First Number + second Number : ", num1 + num2)
    else:
        print("Sorry! I can't process your request")

# Substraction of Two Numbers
subsCondition = input("For Substraction Press 2 : ")

if(subsCondition == "2"):
    print("First Number - Second Number = ", num1 - num2)
else:
    print("Please Enter 2")
    print(input("Enter - 2 : "))
    if(print(input("Enter - 2 : ")) == "2"):
        print("First Number - second Number : ", num1 - num2)
    else:
        print("Sorry! I can't process your request")

# Multiplicatin of Two Numbers
multCondition = input("For Multiplication Press 3 : ")

if(multCondition == "3"):
    print("First Number x Second Number = ", num1 * num2)
else:
    print("Please Enter 3")
    print(input("Enter - 3 : "))
    if(print(input("Enter - 3 : ")) == "3"):
        print("First Number x second Number : ", num1 * num2)
    else:
        print("Sorry! I can't process your request")

# Divide of Two Numbers
divCondition = input("For Divide Press 4 : ")

if(divCondition == "4"):
    print("First Number / Second Number = ", num1 / num2)
else:
    print("Please Enter 4")
    print(input("Enter - 4 : "))
    if(print(input("Enter - 4 : ")) == "4"):
        print("First Number / second Number : ", num1 / num2)
    else:
        print("Sorry! I can't process your request")


# =====================================================================
# VERSION 2: The Match-Case Approach
# =====================================================================

print("--- Welcome to the Legacy Match-Case Calculator ---")
num1 = int(input("Enter Your First Number : "))
num2 = int(input("Enter Your Second Number : "))

print("For Addition Press 1")
print("For Substraction Press 2")
print("For Multiply Press 3")
print("For Divide Press 4")

add = int(input("Enter : "))

# First Match Case Statement Block
match add:
    case 1:
        print("Result:", num1 + num2) 
    case 2:
        print("Result:", num1 - num2)
    case 3:
        print("Result:", num1 * num2)
    case 4:
        print("Result:", num1 / num2)
    
    # Fallback Case if user enters wrong number
    case _ if add > 4:
        chance1 = int(input("Please Enter 1 to 4 : "))

        match chance1:
            case 1:
                print("The Sum of", num1, "and", num2, "is", num1 + num2)
            case 2:
                print("The Substraction of", num1, "and", num2, "is", num1 - num2)
            case 3:
                print("The Multiplication of", num1, "and", num2, "is", num1 * num2)
            case 4:
                print("The Divide of", num1, "and", num2, "is", num1 / num2)
            case _ if chance1 > 4:
                print("Sorry! Try Again")
            case _ if chance1 <= 0:
                print("Sorry! Try Again")


# 🤣🤣 THE LEGENDARY COMMENT: 
# More Same Match Case Statement because I didn't use For or While Loop
add = int(input("\nEnter again to continue without loops : ")) 

# Second Match Case Statement Block (Manually Unrolled Loop)
match add:
    case 1:
        print("Result:", num1 + num2) 
    case 2:
        print("Result:", num1 - num2)
    case 3:
        print("Result:", num1 * num2)
    case 4:
        print("Result:", num1 / num2)

    case _ if add > 4:
        chance1 = int(input("Please Enter 1 to 4 : "))

        match chance1:
            case 1:
                print("The Sum of", num1, "and", num2, "is", num1 + num2)
            case 2:
                print("The Substraction of", num1, "and", num2, "is", num1 - num2)
            case 3:
                print("The Multiplication of", num1, "and", num2, "is", num1 * num2)
            case 4:
                print("The Divide of", num1, "and", num2, "is", num1 / num2)
            case _ if chance1 > 4:
                print("Sorry! Try Again")
            case _ if chance1 <= 0:
                print("Sorry! Try Again")

# More Same Match Case Statement because I didn't use For or While Loop
"""
=============================================================================
Day 4: If-Else Branching, Match Case & Built-in Modules
=============================================================================
This module covers decision-making in Python using conditional statements, 
structural pattern matching (Python 3.10+), and importing standard modules.
"""

# ---------------------------------------------------------
# 1. IF-ELSE BRANCHING (Nested Conditions)
# ---------------------------------------------------------
# Handing branching in a program based on specific conditions.
# Example: A simple Login System

print("--- Login System ---")
email = input("Enter your email: ")
password = input("Enter your password: ")

if email == 'nitesh.campusx@gmail.com' and password == '12345':
    print("Welcome!")

elif email == 'nitesh.campusx@gmail.com' and password != '12345':
    print("Please enter the correct password.")
    
    # Nested if-else for a second attempt
    password = input("Enter password again: ")
    if password == '12345':
        print("Welcome!")
    else:
        print("Beta tumse na ho payega.") # Access Denied 😂

else:
    print("Chal nikal.") # Unrecognized Email


# ---------------------------------------------------------
# 2. LOGICAL CONDITIONS (Finding Minimum)
# ---------------------------------------------------------
print("\n--- Find Minimum of 3 Numbers ---")
a = int(input("First num: "))
b = int(input("Second num: "))
c = int(input("Third num: "))

if a < b and a < c:
    print('Smallest is', a)
elif b < c:
    print('Smallest is', b)
else:
    print('Smallest is', c)


# ---------------------------------------------------------
# 3. SIMPLE CALCULATOR (If-Elif-Else Ladder)
# ---------------------------------------------------------
print("\n--- Basic Calculator ---")
fnum = int(input("Enter the first num: "))
snum = int(input("Enter the second num: "))
op = input('Enter the operation (+, -, *, /): ')

if op == '+':
    print(f"Result: {fnum + snum}")
elif op == '-':
    print(f"Result: {fnum - snum}")
elif op == '*':
    print(f"Result: {fnum * snum}")
elif op == '/':
    if snum != 0:
        print(f"Result: {fnum / snum}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid Operator!")


# ---------------------------------------------------------
# 4. MENU DRIVEN PROGRAM
# ---------------------------------------------------------
print("\n--- ATM Menu Simulation ---")
menu = input("""
Hi! How can I help you today?
1. Enter 1 for Pin Change
2. Enter 2 for Balance Check
3. Enter 3 for Withdrawal
4. Enter 4 for Exit
Select an option: """)

if menu == '1':
    print("Process: Pin Change initiated.")
elif menu == '2':
    print("Process: Fetching Account Balance.")
elif menu == '3':
    print("Process: Withdrawal initiated.")
elif menu == '4':
    print("Exiting... Have a nice day!")
else:
    print("Invalid Input. Please select a valid option.")


# ---------------------------------------------------------
# 5. MATCH CASE STATEMENTS (Python 3.10+)
# ---------------------------------------------------------
# A cleaner alternative to long if-elif-else ladders (similar to switch-case).

print("\n--- Match Case Demonstration ---")
x = int(input("Enter a number to match: "))

match x:
    case 0:
        print("x is absolute zero")
    case 4:
        print("Exact match: case is 4")
    case _ if x != 90: # Using conditions inside cases
        print(f"{x} is definitely not 90")
    case _ if x != 80:
        print(f"{x} is definitely not 80")
    case _: # The default/wildcard case (Executes if nothing else matches)
        print(f"Default case triggered for: {x}")


# ---------------------------------------------------------
# 6. PYTHON BUILT-IN MODULES
# ---------------------------------------------------------
# Python comes with a massive standard library. We can import and use them.
print("\n--- Built-in Modules ---")

# 1. math module
import math
print("Factorial of 5:", math.factorial(5))
print("Floor of 6.8:", math.floor(6.8))
print("Square root of 25:", math.sqrt(25))

# 2. keyword module
import keyword
print("\nPython Keywords (First 10):", keyword.kwlist[:10], "...")

# 3. random module
import random
print("\nRandom number between 0 and 100:", random.randint(0, 100))

# 4. datetime module
import datetime
print("\nCurrent Date and Time:", datetime.datetime.now())

# Note: To see all available modules in your Python environment, uncomment the line below:
# help('modules')
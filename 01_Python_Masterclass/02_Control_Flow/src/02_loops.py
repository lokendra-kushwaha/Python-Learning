"""
=============================================================================
Day 5: Loops in Python
=============================================================================
This module covers iterative execution using 'while' and 'for' loops.
It includes loop controls (break, continue, pass), nested loops, 
pattern printing, and practical examples like a guessing game.
"""

# ---------------------------------------------------------
# 1. WHILE LOOP
# ---------------------------------------------------------
# 'while' loops execute a block of code as long as a condition is True.
# Use Case: Displaying content dynamically when the exact number of iterations is unknown.

print("--- Multiplication Table ---")
num = int(input("Enter the number for the table: "))
i = 0
while i < 10:
    print(num * (i + 1))
    i = i + 1

# --- While Loop with Else ---
# The 'else' block executes ONLY if the loop finishes naturally (without a 'break').
print("\n--- While-Else Demonstration ---")
x = 1
while x < 3:
    print(f"Value of x: {x}")
    x += 1
else:
    print("Limit crossed. Loop finished naturally.")

# --- Practical Example: Number Guessing Game --- 
import random
print("\n--- Number Guessing Game ---")
jackpot = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Wrong! Guess higher.")
    else:
        print("Wrong! Guess lower.")
    
    guess = int(input("Guess again: "))
    counter += 1
else:
    print(f"Correct Guess! You won the jackpot: {jackpot}")
    print(f"Total Attempts: {counter}")


# ---------------------------------------------------------
# 2. FOR LOOP
# ---------------------------------------------------------
# 'for' loops are used for iterating over a sequence (like a list, tuple, string, or range).

print("\n--- For Loop with Range ---")
for i in range(1, 14, 3):  # Start: 1, End: 13, Step: 3
    print(i, end=" ")
print()

for i in range(10, 0, -1): # Reverse loop
    print(i, end=" ")
print()

print("\n--- Iterating Over Different Data Types ---")
for i in 'Delhi':          # String iteration
    print(i, end=" ")
print()

for i in [1, 2, 3]:        # List iteration
    print(i, end=" ")
print()

for i in (1, 14, 3):       # Tuple iteration
    print(i, end=" ")
print()

for i in {1, 14, 3}:       # Set iteration (Unordered)
    print(i, end=" ")
print()

for i in {1: 'A', 2: 'B'}: # Dictionary iteration (Iterates over keys by default)
    print(i, end=" ")
print()

# --- Depreciation Example ---
print("\n--- Depreciation Calculation ---")
current = 10000
for i in range(10, 0, -1):
    print(f"Year {i}: Remaining Value = {current:.2f}")
    current = current / 1.1


# ---------------------------------------------------------
# 3. MATHEMATICAL SERIES & NESTED LOOPS
# ---------------------------------------------------------

# --- Math Series Example ---
print("\n--- Math Series Calculation ---")
n = int(input("Enter n for series sum: "))
result = 0
fact = 1
for i in range(1, n + 1):
    fact = fact * i
    result = result + (i / fact)
print(f"Result of series: {result}")

# --- Nested Loop ---
print("\n--- Nested Loop (Cartesian Product) ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end="  ")
    print()

# --- Pattern 1: Right-Angled Triangle ---
print("\n--- Pattern 1 ---")
rows1 = int(input("Enter no. of rows for Star Pattern: "))
for i in range(1, rows1 + 1):
    for j in range(1, i + 1):
        print("*", end='')
    print()

# --- Pattern 2: Number Palindrome Triangle ---
print("\n--- Pattern 2 ---")
rows2 = int(input("Enter no. of rows for Number Pattern: "))
for i in range(1, rows2 + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for k in range(i - 1, 0, -1):
        print(k, end='')
    print()


# ---------------------------------------------------------
# 4. LOOP CONTROL STATEMENTS
# ---------------------------------------------------------

# --- 1. Break Statement ---
# Exits the loop entirely. Useful for linear searching.
print("\n--- Break Statement ---")
for i in range(1, 10):
    if i == 5:
        print("Breaking loop at 5")
        break
    print(i, end=" ")
print()

# Practical use of Break + For-Else (Prime Number Generator)
print("\n--- Prime Number Generator ---")
lower = int(input("Lower range: "))
upper = int(input("Upper range: "))
print(f"Prime numbers between {lower} and {upper}:")
for i in range(lower, upper + 1):
    if i < 2:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
print()

# --- 2. Continue Statement ---
# Skips the current iteration and moves to the next.
# Practical Use: Skipping a product that is out of stock in an e-commerce loop.
print("\n--- Continue Statement ---")
for i in range(1, 10):
    if i == 5:
        continue # 5 will not be printed
    print(i, end=" ")
print()

# --- 3. Pass Statement ---
# A null statement (does nothing). Used as a placeholder for future code.
for i in range(1, 10):
    pass # Code to be added later
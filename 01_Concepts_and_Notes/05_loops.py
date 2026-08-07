#==================================================================================================
#                              Day - 5 : Loops in Python
#==================================================================================================

# <--- Loops in python --->
# Need of loop --> for display content dynamacally 

# While loop -->
num = int(input("Enter the number: "))

i = 0
while i < 10:
    print(num*(i+1))
    i = i + 1

# While loop with else

x = 1

while x < 3:
    print(x)
    x += 1

else:
    print("limit crossed.")

# --- A guessing game --- 

# Generate the random integer between 1 and 100
import random

jackpot = random.randint(1, 100)
guess = int(input("Guess: "))

counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("Wrong! Guess higher")

    else:
        print("Wrong! Guess lower")

    guess = int(input("Guess: "))
    counter += 1

else:
    print("Correct Guess.")
    print("Attempts:", counter)

# for loop -->

for i in range(1, 14, 3):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in 'Delhi':
    print(i)

for i in [1, 2, 3]:
    print(i)

for i in (1, 14, 3):
    print(i)

for i in {1, 14, 3}:
    print(i)

for i in {1:2, 2:3}:
    print(i)

current = 10000

for i in range (10, 0, -1):
    print(i, current)
    current = current/1.1


# <--- Python Strings --->

n = int(input("Enter n: "))

result = 0
fact = 1
for i in range(1, n + 1):
    fact = fact * i
    result = result + i/fact

print(result)

# Nested loop

for i in range(1, 5):
    for j in range(1, 5):
        print(i, j)

# Pattern - 1

rows = int(input("Enter no. of rows: "))

for i in range(1, rows+1):
    for j in range(1, i+1):
        print("*", end='')
    print()

# Pattern - 2

rows = int(input("Enter no. of rows: "))

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end='')
    for k in range(i-1, 0, -1):
        print(k, end='')
    print()

# Loop Control Statements -->

# Break # Uses for Linear searching
for i in range(1, 10):
    if i == 5:
        break
    print(i)

lower = int(input("Lower range: "))
upper = int(input("Upper range: "))

for i in range(lower, upper+1):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        print(i)

# Continue Statement --> Used for skip a product that is out of stock.
for i in range(1, 10):
    if i == 5:
        continue
    print(i)

# Pass statement
for i in range(1, 10):
    pass
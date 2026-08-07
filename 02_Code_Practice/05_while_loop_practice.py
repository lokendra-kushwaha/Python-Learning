"""
Topic: While Loop Variations
Goal: To practice condition-controlled loops, taking continuous user input, incrementing/decrementing counters, and the while-else construct.
"""

# -------------------------------------------------------------
# 1. Continuous User Input: 
# The loop keeps asking for input as long as the number is <= 38.
# -------------------------------------------------------------
i = int(input("Enter the number: "))
print(i)
while(i<=38):
    i = int(input("Enter the number: "))
    print(i)

print("Done with the loop")
print("-" * 30)

# -------------------------------------------------------------
# 2. Incrementing Counter: 
# Takes a starting number and automatically increments it by 1 until it reaches 38.
# -------------------------------------------------------------
i = int(input("Enter the Number: "))
while(i<=38):
    print(i)
    i = i + 1

print("-" * 30)

# -------------------------------------------------------------
# 3. Decrementing Counter with While-Else: 
# Loop runs until count is 0. The 'else' block executes ONLY when the loop condition becomes False naturally.
# -------------------------------------------------------------
count = 5
while (count > 0):
    print(count)
    count = count - 1

else:
    print("I am inside else")
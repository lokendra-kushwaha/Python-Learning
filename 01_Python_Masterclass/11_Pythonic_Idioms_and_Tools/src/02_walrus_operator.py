"""
====================================================================================
🦭 PYTHONIC IDIOMS: THE WALRUS OPERATOR (:=)
====================================================================================
Description: Introduced in Python 3.8, the Walrus Operator allows you to 
             assign a value to a variable AND return that value in the same expression.
             It makes code shorter, cleaner, and more "Pythonic".
====================================================================================
"""

def section_divider(title):
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")

# 🟢 1. IN IF-STATEMENTS (Avoiding separate assignment)
# ====================================================================================
section_divider("1. THE WALRUS IN 'IF' STATEMENTS")

fruits = ['apple', 'banana', 'mango', 'orange', 'grape']

print("-> The Old Way (2 steps):")
n = len(fruits)
if n > 3:
    print(f"   List is long enough. It has {n} items.")

print("\n-> The Walrus Way (1 step):")
# The variable 'count' is assigned AND checked in the exact same line!
if (count := len(fruits)) > 3:
    print(f"   List is long enough. It has {count} items.")


# 🟢 2. IN LIST COMPREHENSIONS (Optimizing expensive calculations)
# ====================================================================================
"""
CONCEPT: 
Sometimes we want to filter a list based on a heavy calculation, and also save 
that calculated result. Without the walrus, we have to run the function twice!
"""
section_divider("2. THE WALRUS IN LIST COMPREHENSIONS")

def expensive_calculation(x):
    """Simulates a heavy mathematical function"""
    return x ** 3

numbers = [2, 3, 4, 5]

print("-> The Old Way (Runs the function TWICE per item):")
# Calculates expensive_calculation(x) once for the condition, and once for the output
old_result = [expensive_calculation(x) for x in numbers if expensive_calculation(x) > 50]
print(f"   Result: {old_result}")

print("\n-> The Walrus Way (Runs the function ONCE per item):")
# Calculates once, assigns it to 'cube', and reuses 'cube' for the output!
smart_result = [cube for x in numbers if (cube := expensive_calculation(x)) > 50]
print(f"   Result: {smart_result}")


# 🟢 3. IN WHILE-LOOPS (Cleaning up repeated inputs)
# ====================================================================================
section_divider("3. THE WALRUS IN 'WHILE' LOOPS")
print("-> Type some words below. Type 'quit' to exit the loop.\n")

# Instead of writing the input statement twice (before the loop and inside the loop),
# the walrus handles both the assignment and the condition check right here!
while (user_input := input("Enter a word: ")) != "quit":
    print(f"   ✅ You entered: {user_input}")


print("\n" + "=" * 60)
print("🎯 CONCLUSION: The Walrus (:=) saves lines of code and reduces duplicate calculations!")
print("=" * 60)
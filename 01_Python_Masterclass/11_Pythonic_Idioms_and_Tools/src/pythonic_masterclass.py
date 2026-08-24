# 🌟 ================================================================================= 🌟
# 🚀                PYTHONIC IDIOMS & PRO-TOOLS --> MASTERCLASS
# 🌟 ================================================================================= 🌟

# 📝 1. PEP 8 (Python Enhancement Proposal 8)
# Concept: PEP 8 is NOT code. It is the official "Style Guide" for writing Python code. 
# It ensures consistency across developers globally. 
# Key Rules:
# - Use 4 spaces for indentation (not tabs).
# - Variables/Functions: snake_case (e.g., `my_var`, `calculate_sum()`).
# - Classes: PascalCase (e.g., `MyClass`, `DatabaseConnection`).
# - Limit all lines to a maximum of 79 characters.


# 📝 2. DOC-STRINGS (Documentation Strings)
# Concept: A string literal that occurs as the first statement in a module, function, class, or method definition.

def calculate_power(base, exp):
    """
    Calculates the power of a number.
    
    Args:
        base (int): The base number.
        exp (int): The exponent.
        
    Returns:
        int: The result of base raised to the power of exp.
    """
    return base ** exp

print("Doc-string output:")
print(calculate_power.__doc__) # You can access it programmatically!


# 🔤 3. F-STRINGS (Formatted String Literals)
# Concept: Introduced in Python 3.6, it is the fastest and most readable way to format strings. 
# You can execute Python expressions directly inside the `{}`.

name = "Lokendra"
age = 20
# Old way: "My name is {} and I am {} years old.".format(name, age)
# Pythonic way:
print(f"\nF-String output: My name is {name} and in 5 years I will be {age + 5} years old.") 
letter = "Hey my name is {1} and I am form {0}"
country = "India"
name = "Lokendra"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am form {country}")
print(f"We use fstrings like this: Hey my name is {{name}} and I am form {{country}}")

price = 49.89999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())

print(type(f"{2 * 30}"))

# ⚡ 4. SHORT-HAND IF-ELSE (Ternary Operator)
# Concept: Compresses a simple if-else block into a single line. 
# Syntax: [Value_if_True] if [Condition] else [Value_if_False]

num = 15
# Pythonic way:
result = "Even" if num % 2 == 0 else "Odd"
print(f"\nTernary output: The number is {result}")


# 🔄 5. THE 'FOR...ELSE' LOOP (The Search Engine Logic)
# 🧠 EXPLANATION: This is heavily asked in interviews! 
# The `else` block executes ONLY IF the `for` loop finishes NATURALLY. 
# If the loop is broken using the `break` keyword, the `else` block is SKIPPED.

def search_item(data_list, target):
    for item in data_list:
        if item == target:
            print(f"\nFor...Else output: Target {target} FOUND! Breaking loop.")
            break
    else:
        # This only runs if the loop NEVER hit the 'break' statement
        print(f"\nFor...Else output: Target {target} NOT FOUND in the database.")

search_item([10, 20, 30], 20) # Hits break, skips else
search_item([10, 20, 30], 99) # Finishes naturally, runs else


# 🔢 6. ENUMERATE FUNCTION
# Concept: When looping through an iterable, you often need both the ITEM and its INDEX.
# Instead of initializing a counter variable `i = 0` manually, use `enumerate()`.

heroes = ["Iron Man", "Batman", "Spider-Man"]
print("\nEnumerate output:")
for index, hero in enumerate(heroes, start=1): 
    # start=1 changes the starting index from 0 to 1
    print(f"Rank {index}: {hero}")


# 🔍 7. INTROSPECTION TOOLS (dir(), __dict__, help())
# Concept: The "X-Ray Vision" of Python. These tools let you look inside objects while the code is running.

class Robot:
    def __init__(self, name):
        self.name = name
        self.battery = 100
        
    def walk(self):
        pass

jarvis = Robot("Jarvis")

print("\n--- Introspection Tools ---")

# A. dir() -> Returns a list of ALL attributes and methods (including dunder methods) of the object.
print("dir(jarvis) ->", dir(jarvis)[:5], "... (truncated)") 

# B. __dict__ -> Returns the object's Local Namespace as a Dictionary!
# 🧠 EXPLANATION: Remember your "Namespaces" module? This is EXACTLY where Python stores the instance variables in the RAM!
print("__dict__ output ->", jarvis.__dict__) # Output: {'name': 'Jarvis', 'battery': 100}

# C. help() -> Reads the Doc-Strings and creates a built-in manual for the object.
# help(jarvis) # Uncomment this to see the full manual in the terminal!

# 🌟 ================================================================================= 🌟
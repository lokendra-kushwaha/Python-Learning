"""
=============================================================================
Day 2: Datatypes and Variables
=============================================================================
This module covers fundamental Python concepts including built-in data types, 
variables, dynamic typing vs. binding, keywords, identifiers, user input, 
and type conversion.
"""

# ---------------------------------------------------------
# 1. CORE DATA TYPES
# ---------------------------------------------------------
# Python supports multiple built-in data types for handling numbers, text, and collections.

# Numeric and Boolean types
print(1e308)     # Maximum integer/float magnitude handled cleanly before overflow
print(1.7e308)   # Floating-point upper limit approximation in standard Python builds
print(True)      # Boolean True (subclass of integer 1)
print(False)     # Boolean False (subclass of integer 0)
print("lokendra")# String datatype for handling text
print(5 + 6j)    # Complex number datatype (real + imaginary part)

# Collection types
print([1, 2, 3]) # List: Ordered, mutable collection (backed by array structures in CPython)
print((1, 2, 3)) # Tuple: Ordered, immutable collection
print({1, 2, 3}) # Set: Unordered collection of unique items
print({1: 2, 3: 4})# Dictionary: Key-value pair mapping structure

# Checking the type of an object using the built-in type() function
print(type(3))   # Output: <class 'int'>


# ---------------------------------------------------------
# 2. VARIABLES, DYNAMIC TYPING & DYNAMIC BINDING
# ---------------------------------------------------------
# Variables are symbolic containers used to store data values for future reference.
name = 'nitesh'
print(name)

a = 5
b = 6
print(a + b)

# Dynamic Typing:
# Python does not require explicit declaration of a variable's data type 
# prior to assignment (unlike static typing in C/Java like 'int a = 5;').
a = 5 

# Dynamic Binding:
# A variable name can reference objects of different data types at different times 
# during execution, unlike static binding found in languages like C++ or Java.
a = 5
print(a)

a = 'nitesh' # Re-binding the same variable name to a string object
print(a)

# Multiple variable assignments in a single line
a = 1
b = 2
c = 3
print(a, b, c)

a, b, c = 1, 2, 3  # Packed assignment
print(a, b, c)

a = b = c = 5      # Chained assignment
print(a, b, c)


# ---------------------------------------------------------
# 3. KEYWORDS AND IDENTIFIERS
# ---------------------------------------------------------
# Keywords: Reserved words in Python that have special meaning (e.g., if, else, return).
# Execution Model: Python is an interpreted language (code executed line-by-line via interpreter) 
# unlike C or Java which use compilers to translate the entire code into low-level machine code at once.

# Identifiers (Naming rules):
# Rule 1: Cannot start with a digit.
# 1name = 'nitesh'  # SyntaxError
name1 = 'nitesh'    # Valid

# Rule 2: Special characters are not allowed except for the underscore ('_').
# first-name = 'lokendra'  # SyntaxError due to hyphen
first_name = 'lokendra'    # Valid

_ = 'lokendra'             # Underscore alone is a valid identifier
print(_)

# Rule 3: Identifiers cannot share names with Python keywords.


# ---------------------------------------------------------
# 4. USER INPUT & TYPE CONVERSION
# ---------------------------------------------------------
# Dynamic software interacts interactively with users (e.g., input collection).

# input() function always returns user input as a string data type.
fnum = input("Enter first number: ")
snum = input("Enter second number: ")

# Explicit type conversion using int() to parse strings into integers for arithmetic addition
add = int(fnum) + int(snum)
print("Sum:", add)
print("Type of fnum input:", type(fnum)) 
# Note: Type conversion functions create a brand-new converted value in memory; 
# they do not mutate the original variable's type directly.

# Type Conversion Types:
# 1. Implicit Conversion: Handled automatically by the Python interpreter.
print(5 + 5.6)                     # Integer 5 is implicitly promoted to float (5.0)
print(type(5), type(5.6))

# 2. Explicit Conversion (Type Casting): Done manually using built-in functions like int(), float(), str().
print(int('4'))                    # Converts string '4' explicitly to integer 4
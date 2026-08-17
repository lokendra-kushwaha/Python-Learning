"""
=============================================================================
Day 1: Print Statements, Comments & Escape Sequences
=============================================================================
This module covers the absolute basics of Python: displaying output, 
writing code comments, and handling special string characters.
"""

# ---------------------------------------------------------
# 1. THE PRINT FUNCTION
# ---------------------------------------------------------
# print() is a built-in Python function used to display data (strings, ints, etc.) on the console.

# Using the 'end' parameter:
# By default, print() adds a new line (\n) at the end. 
# 'end' replaces that new line with a custom character (like a space).
print("Lokendra Kushwaha", end=' ') 
print("is Male")  # Output: Lokendra Kushwaha is Male

# Using the 'sep' parameter:
# By default, multiple arguments in print() are separated by a space.
# 'sep' allows us to define a custom separator (like '*').
print('I', 'am', 'a', 'developer.', sep='*') 
# Output: I*am*a*developer.


# ---------------------------------------------------------
# 2. COMMENTS
# ---------------------------------------------------------
# Comments are notes written for developers. The Python interpreter completely ignores them.

# This is a single-line comment.
print("Hello World!") # This prints a greeting.


# ---------------------------------------------------------
# 3. ESCAPE SEQUENCES
# ---------------------------------------------------------
# Escape characters (starting with \) are used to insert characters that are otherwise illegal in a string.

# To print double quotes inside a string, use \" or wrap the string in single quotes.
print("He said, \"I want to eat.\"")  
print('He said, "I want to eat."')    

# Using \n for a new line within the same string:
print("He is a \"good boy\" \nand she is also a \"good girl.\"")
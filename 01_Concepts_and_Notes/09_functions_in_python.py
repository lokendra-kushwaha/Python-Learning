#=============================================================================
#                           Day 9: Functions in Python
#=============================================================================
# A function is a block of reusable code that runs only when it is called.
# You can pass data, known as parameters, into a function.

# ----------------------------------------------------------------------------
# 1. Basic Function Setup & Docstrings
# ----------------------------------------------------------------------------
def is_even(num):
    """
    Checks if a given number is even or odd.
    
    Parameters:
    num (int): Any valid integer.
    
    Returns:
    str: 'even' if the number is divisible by 2, 'odd' otherwise.
         Returns an error message if the input is not an integer.
         
    Created on: 12th August 2026
    """
    if type(num) == int:
        if num % 2 == 0:
            return 'even'
        else:
            return 'odd'
    else:
        return "Invalid Input! Integer required."

# Accessing the docstring of a function using the magic attribute doc
print("--- Docstrings ---")
print(is_even.__doc__)
print(print.__doc__) # Accessing built-in function's docstring

print("\n--- Function Execution ---")
print(f"Is 34 even? {is_even(34)}")

# Using the function in a loop
for i in range(1, 6):
    print(f"{i} is {is_even(i)}")


# ----------------------------------------------------------------------------
# 2. Types of Arguments
# ----------------------------------------------------------------------------
# Defining the function once to demonstrate different ways to call it
def power(a=1, b=0):
    """Returns 'a' raised to the power of 'b'. Default values are provided."""
    return a ** b

print("\n--- Argument Types ---")
# A. Default Arguments (Uses the default value if none is passed)
print(f"Default Args (2, None): {power(2)}") 
print(f"Default Args (None): {power()}")     

# B. Positional Arguments (Order strictly matters: a=2, b=3)
print(f"Positional Args (2, 3): {power(2, 3)}")

# C. Keyword Arguments (Order doesn't matter, assigned via keys)
print(f"Keyword Args (b=3, a=2): {power(b=3, a=2)}")


# ----------------------------------------------------------------------------
# 3. *args and **kwargs (Variable Length Arguments)
# ----------------------------------------------------------------------------
# *args: Allows passing a variable number of non-keyword arguments (Tuple)
def multiply(*args): 
    """Multiplies all the numbers passed as arguments."""
    product = 1
    for i in args:
        product *= i
    return product

print("\n--- *args ---")
print(f"Multiplying 3 numbers: {multiply(2, 3, 3)}")
print(f"Multiplying 7 numbers: {multiply(2, 3, 3, 3, 5, 3, 8)}")

# **kwargs: Allows passing any number of keyword arguments (Dictionary)
def display(**kwargs): 
    """Displays key-value pairs passed as keyword arguments."""
    print("\n--- **kwargs ---")
    for key, value in kwargs.items():
        print(f"{key.capitalize()} -> {value.capitalize()}")
    
display(india='delhi', srilanka='colombo', nepal='kathmandu', pakistan='islamabad')


# ----------------------------------------------------------------------------
# 4. Methods Returning None
# ----------------------------------------------------------------------------
# Some list operations change the list in-place but return 'None'
print("\n--- Return Value of In-place Methods ---")
L = [1, 2, 3]
print(f"Return value of L.append(4): {L.append(4)}") # Output is None
print(f"Updated List L: {L}")


# ----------------------------------------------------------------------------
# 5. Nested Functions & Scope
# ----------------------------------------------------------------------------
print("\n--- Nested Functions ---")
def outer_func():
    def inner_func():
        print("Inside inner_func (g)")
        # outer_func() # ❌ Recursion error if not handled properly
    
    inner_func() # inner_func is accessible only inside outer_func
    print("Inside outer_func (f)")

outer_func()
# inner_func() # ❌ Throws NameError: name 'inner_func' is not defined (Out of scope)


# ----------------------------------------------------------------------------
# 6. Functions as First-Class Citizens
# ----------------------------------------------------------------------------
# In Python, functions are treated just like variables/datatypes.
def square(num):
    return num ** 2

print("\n--- First-Class Citizens ---")
print(f"Type of function: {type(square)}")
print(f"Memory ID of function: {id(square)}")

# A. Aliasing (Assigning function to a new variable)
x = square
print(f"Executing aliased function x(3): {x(3)}")

# B. Deleting a function from memory
del square
# print(square(3)) # ❌ Throws NameError as the function is deleted

# C. Storing functions in Data Structures (Lists, Sets)
def cube(num):
    return num ** 3

func_list = [1, 2, 3, cube]
print(f"Executing function from List: {func_list[-1](3)}") # Accesses 'cube' and passes 3

func_set = {cube} # Functions are immutable/hashable, so they can be stored in sets
print(f"Function inside a Set: {func_set}")

# D. Returning a function from a function (Closures)
def get_math_function():
    def add(a, b):
        return a + b
    return add # Returning the reference, not calling it

returned_func = get_math_function()
print(f"Executing returned function: {returned_func(3, 4)}")

# E. Passing a function as an argument
def func_a():
    return "Result from func_a"

def func_b(callback_func):
    print("Inside func_b, calling the passed function...")
    return callback_func()

print(func_b(func_a))


# ----------------------------------------------------------------------------
# 7. Lambda Functions (Anonymous Functions)
# ----------------------------------------------------------------------------
# lambda arguments : expression
print("\n--- Lambda Functions ---")
square_lambda = lambda x: x ** 2
print(f"Lambda Square (2): {square_lambda(2)}")

add_lambda = lambda a, b: a + b
print(f"Lambda Add (5, 2): {add_lambda(5, 2)}")

check_char = lambda s: 'a' in s
print(f"Is 'a' in 'hello'? {check_char('hello')}")

is_even_lambda = lambda x: 'even' if x % 2 == 0 else 'odd'
print(f"Lambda Is Even (2): {is_even_lambda(2)}")


# ----------------------------------------------------------------------------
# 8. Higher Order Functions (HOF)
# ----------------------------------------------------------------------------
# A function that takes another function as an argument or returns a function.
print("\n--- Higher Order Functions ---")

# Creating a custom HOF
def transform(f, L): 
    """Applies a given function 'f' to all items in List 'L'."""
    output = []
    for i in L:
        output.append(f(i))
    return output

my_list = [1, 2, 3, 4]
print(f"Custom HOF (Cube): {transform(lambda x: x**3, my_list)}")


# ----------------------------------------------------------------------------
# 9. Built-in Higher Order Functions (Map, Filter, Reduce)
# ----------------------------------------------------------------------------
print("\n--- Map, Filter, Reduce ---")

# Map: Applies a function to every item in an iterable.
# map(function, iterable)
mapped_list = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', [1, 2, 3, 4, 5]))
print(f"Map Result: {mapped_list}")

# Filter: Returns items from an iterable for which the function returns True.
# filter(function, iterable)
L2 = [1, 2, 3, 4, 5, 6, 7]
filtered_list = list(filter(lambda x: x > 5, L2))
print(f"Filter Result (> 5): {filtered_list}")

fruits = ['apple', 'guava', 'cherry', 'apricot']
a_fruits = list(filter(lambda x: x.startswith('a'), fruits))
print(f"Filter Result (starts with 'a'): {a_fruits}")

# Reduce: Applies a rolling computation to sequential pairs of values in an iterable.
# reduce(function, iterable) -> Needs to be imported from functools
import functools

sum_all = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(f"Reduce Result (Sum): {sum_all}")

find_min = functools.reduce(lambda x, y: x if x < y else y, [23, 11, 45, 10, 1])
print(f"Reduce Result (Minimum): {find_min}")

#=============================================================================
# End of File
#=============================================================================
#=============================================================================
#                           Python Functions Practice
#=============================================================================

# ----------------------------------------------------------------------------
# 1. Basic Functions & The 'pass' Keyword
# ----------------------------------------------------------------------------

def calculateGmean(a, b):
    """
    Calculates a custom mean using the formula: (a*b)/(a+b).
    (Note: Actual Geometric Mean mathematically is sqrt(a*b))
    """
    mean = (a * b) / (a + b)
    print(f"Calculated Mean of {a} and {b} is: {mean}")

def isGreater(a, b):
    """Checks and prints which number is greater."""
    if a > b:
        print(f"{a} (First number) is greater than {b}")
    else:
        print(f"{b} (Second number) is greater or equal to {a}")

def isLesser(a, b):
    """
    Placeholder function.
    'pass' is used when we want to write the function body later 
    without getting an indentation error.
    """
    pass

print("--- Basic Functions Execution ---")
a = 9
b = 8

# Using functions instead of writing repetitive if-else blocks
isGreater(a, b)
calculateGmean(a, b)

print("\n--- Reusing the same functions for new variables ---")
c = 8
d = 7
isGreater(c, d)
calculateGmean(c, d)


# ----------------------------------------------------------------------------
# 2. Default Arguments
# ----------------------------------------------------------------------------

def average_with_defaults(a=1, b=1, c=1):
    """Calculates average of 3 numbers. Uses default value 1 if not provided."""
    avg = (a + b + c) / 3  # Divided by 3 instead of 2 for correct average
    print(f"The average (with defaults) is: {avg}")

print("\n--- Default Arguments ---")
average_with_defaults(4, 6)      # a=4, b=6, c=1 (default)
average_with_defaults(b=9)       # a=1 (default), b=9, c=1 (default)


# ----------------------------------------------------------------------------
# 3. Variable-Length Positional Arguments (*args)
# ----------------------------------------------------------------------------

def average_with_args(*numbers):
    """
    Accepts any number of arguments as a Tuple and calculates their average.
    """
    print(f"Data type of *numbers is: {type(numbers)}")
    sum_val = 0
    for i in numbers:
        sum_val = sum_val + i

    avg = sum_val / len(numbers)
    print(f"Average of {numbers} is: {avg}")
    return avg

print("\n--- *args Execution ---")
# Capturing the returned value in a variable
result = average_with_args(5, 6, 7, 8, 8)
print(f"Returned value from function: {result}")


# ----------------------------------------------------------------------------
# 4. Variable-Length Keyword Arguments (**kwargs)
# ----------------------------------------------------------------------------

def print_full_name(**name):
    """
    Accepts any number of keyword arguments as a Dictionary.
    """
    # name is treated as a dictionary inside this function
    print("\n--- **kwargs Execution ---")
    print(f"Data type of **name is: {type(name)}")
    print("Hello,", name["fname"], name["mname"], name["lname"])

# Passing arguments with keys
print_full_name(mname="Buchanan", lname="Barnes", fname="James")

#=============================================================================
# End of File
#=============================================================================
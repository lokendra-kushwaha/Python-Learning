"""
Custom Min Function
-------------------
A script that reverse-engineers Python's built-in min() function.
It finds the smallest item in an iterable.
"""

import functools
from typing import Iterable, Any

def custom_min(iterable: Iterable) -> Any:
    """
    Finds the smallest item in an iterable.
    
    How it works:
    It directly compares the elements inside the iterable without using 
    ASCII conversion, making it dynamic for strings, lists, and other 
    sequence types. It uses functools.reduce to run the comparison.
    
    Args:
        iterable (Iterable): A sequence (like a string, list, or tuple) to evaluate.
        
    Returns:
        Any: The smallest item found in the iterable.
        
    Raises:
        ValueError: If the iterable is empty.
    """
    # Checking if the iterable is empty (works for lists, strings, tuples, etc.)
    if not iterable:
        raise ValueError("custom_min() arg is an empty sequence")

    # Compare and find the minimum value directly using reduce
    min_value = functools.reduce(lambda x, y: x if x < y else y, iterable)
    
    return min_value

# Testing the function
if __name__ == "__main__":
    # Testing with a string
    S = 'lokendra'
    string_result = custom_min(S)
    print(f"Original String: '{S}'")
    print(f"Minimum Character: '{string_result}'\n")
    
    # Testing with a list of numbers
    numbers = [45, 12, 89, 2, 34]
    num_result = custom_min(numbers)
    print(f"Original List: {numbers}")
    print(f"Minimum Number: {num_result}")
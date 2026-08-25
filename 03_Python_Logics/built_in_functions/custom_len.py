"""
Custom Len Function
-------------------
A script that reverse-engineers Python's built-in len() function.
It counts the total number of items in an iterable.
"""

from typing import Iterable

def custom_len(iterable: Iterable) -> int:
    """
    Calculates the length of an iterable without using Python's built-in len() function.

    How it works:
    Initializes a counter variable to 0. A for loop iterates through the iterable 
    item by item, incrementing the counter by 1 for every iteration.

    Args:
        iterable (Iterable): A sequence or collection (like a string, list, tuple, etc.).

    Returns:
        int: The total number of items in the iterable.
    """
    if not iterable:
        raise ValueError("custom_len() arg is an empty sequence")

    total_length = 0
    # Iterating over any iterable (string, list, tuple, etc.)
    for item in iterable:
        total_length += 1
        
    return total_length

if __name__ == "__main__":
    # Testing with a string
    text = 'Lokendra Kushwaha'
    print(f"Length of string '{text}': {custom_len(text)}")
    
    # Testing with a list
    numbers_list = [1, 2, 3]
    print(f"Length of list {numbers_list}: {custom_len(numbers_list)}")
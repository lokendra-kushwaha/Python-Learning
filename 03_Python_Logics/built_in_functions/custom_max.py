"""
Custom Max Function
-------------------
A script that reverse-engineers Python's built-in max() function.
It finds the largest item in an iterable.
"""

import functools
from typing import Iterable, Any

def custom_max(iterable: Iterable) -> Any:
    """
    Finds the largest item in an iterable.

    This function decodes the true generic logic behind Python's built-in 
    `max()` function. It works on strings, lists of numbers, and other 
    iterables by directly comparing the elements using `functools.reduce`.

    Args:
        iterable: A sequence (like a string, list, or tuple) to evaluate.

    Returns:
        The largest item found in the iterable.

    Raises:
        ValueError: If the iterable is empty.
    """
    # Checking if the iterable is empty (works for lists, strings, tuples, etc.)
    if not iterable:
        raise ValueError("custom_max() arg is an empty sequence")

    # Using reduce to find the maximum value directly
    result = functools.reduce(lambda x, y: x if x > y else y, iterable)
    
    return result


if __name__ == "__main__":
    # Testing with a string
    text = 'lokendra'
    print(f"Max in string '{text}': {custom_max(text)}")

    # Testing with a list of numbers
    numbers = [15, 30, 10, 50, 5]
    print(f"Max in numbers {numbers}: {custom_max(numbers)}")
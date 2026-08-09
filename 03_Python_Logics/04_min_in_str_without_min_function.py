"""
Custom Min Function for Strings
-------------------------------
A script that reverse-engineers Python's built-in min() function for strings.
It finds the lexicographically smallest character in a string using ASCII 
conversion and the reduce function.
"""

import functools

def find_min_char(text: str) -> str:
    """
    Finds the character with the lowest ASCII value in a string.
    
    How it works:
    1. Converts each character to its ASCII integer value using ord().
    2. Uses functools.reduce to run a comparison and find the smallest integer.
    3. Converts that integer back to a character using chr().
    
    Args:
        text (str): The input string to evaluate.
        
    Returns:
        str: The character with the minimum ASCII value. Returns empty string if input is empty.
    """
    if not text:
        return ""

    # Step 1: Convert characters to their ASCII values (Using List Comprehension)
    char_ascii_values = [ord(char) for char in text]
    
    # Step 2: Compare and find the minimum ASCII value using reduce
    min_ascii = functools.reduce(lambda x, y: x if x < y else y, char_ascii_values)
    
    # Step 3: Convert the minimum ASCII value back to a character
    return chr(min_ascii)

# Testing the function
if __name__ == "__main__":
    S = 'lokendra'
    result = find_min_char(S)
    
    print(f"Original String: '{S}'")
    print(f"Minimum Character: '{result}'")
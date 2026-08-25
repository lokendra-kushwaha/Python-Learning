"""
Custom Find Function
--------------------
A script that reverse-engineers Python's built-in string method .find().
It returns the lowest index in the string where the target character is found.
"""

def custom_find_enumerate(text_string: str, target_char: str) -> int:
    """
    Finds the index of a character using the enumerate() function.

    How it works:
    Uses a for loop with enumerate() to iterate through the string and its indices. 
    It checks each character against the target and immediately returns the index 
    upon finding the first match.

    Args:
        text_string (str): The main string to be searched.
        target_char (str): The target character to locate.

    Returns:
        int: The index position of the first occurrence of the target character. 
             Returns -1 if the character is not found.
    """
    for index, char in enumerate(text_string):
        if char == target_char:
            return index

    return -1


def custom_find_range(text_string: str, target_char: str) -> int:
    """
    Finds the index of a character using range() and len().
    
    How it works:
    Generates a range of numbers from 0 to the length of the string.
    Uses these numbers as indices to access and compare each character.
    """
    for index in range(len(text_string)):
        if text_string[index] == target_char:
            return index
            
    return -1


if __name__ == "__main__":
    text = 'lokendra'
    search_char = 'r'
    
    # Testing Method 1
    result1 = custom_find_enumerate(text, search_char)
    print(f"Using enumerate -> Index of '{search_char}' in '{text}': {result1}")
    
    # Testing Method 2
    result2 = custom_find_range(text, search_char)
    print(f"Using range     -> Index of '{search_char}' in '{text}': {result2}")
    
    # Testing a character that doesn't exist
    missing_char = 'z'
    print(f"Missing char '{missing_char}' -> Returns: {custom_find_enumerate(text, missing_char)}")
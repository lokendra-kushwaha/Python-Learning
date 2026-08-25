"""
Custom Remove Prefix Function
-----------------------------
A script that reverse-engineers Python 3.9+ built-in string method .removeprefix().
"""

def custom_removeprefix(text_string: str, prefix: str) -> str:
    """
    Removes a specified prefix from a string if it exists.

    How it works:
    Checks if the beginning of the string matches the prefix using string slicing.
    If it matches, it returns the string sliced from the end of the prefix 
    to the last character. Otherwise, it returns the original string.

    Args:
        text_string (str): The original string.
        prefix (str): The prefix you want to remove.

    Returns:
        str: The modified string without the prefix, or the original string if 
             the prefix wasn't found.
        
    Examples:
        >>> custom_removeprefix('Mr. Lokendra', 'Mr. ')
        'Lokendra'
        >>> custom_removeprefix('Python Developer', 'Java ')
        'Python Developer'
    """
    # Check if the string starts with the given prefix
    if text_string[:len(prefix)] == prefix:
        # Return the string starting from the end of the prefix
        return text_string[len(prefix):]
    
    # If prefix doesn't match, return original string
    return text_string


if __name__ == "__main__":
    # Testing the function
    text1 = "Mr. Lokendra"
    prefix1 = "Mr. "
    print(f"Original: '{text1}'")
    print(f"After removing '{prefix1}': '{custom_removeprefix(text1, prefix1)}'\n")

    text2 = "Lokendra Kushwaha"
    prefix2 = "Dr. "
    print(f"Original: '{text2}'")
    print(f"After removing '{prefix2}': '{custom_removeprefix(text2, prefix2)}")
"""
Custom Remove Suffix Function
-----------------------------
A script that reverse-engineers Python 3.9+ built-in string method .removesuffix().
"""

def custom_removesuffix(text_string: str, suffix: str) -> str:
    """
    Removes a specified suffix from a string if it exists.

    How it works:
    Checks if the end of the string matches the suffix using negative string slicing.
    If it matches, it returns the string sliced from the beginning up to the 
    start of the suffix. Otherwise, it returns the original string.

    Args:
        text_string (str): The original string.
        suffix (str): The suffix you want to remove.

    Returns:
        str: The modified string without the suffix, or the original string if 
             the suffix wasn't found.
        
    Examples:
        >>> custom_removesuffix('lokendra', 'dra')
        'loken'
        >>> custom_removesuffix('python_script.py', '.py')
        'python_script'
    """
    # Handling the edge case where the suffix is empty
    if not suffix:
        return text_string
        
    # Check if the string ends with the given suffix using negative slicing
    if text_string[-len(suffix):] == suffix:
        # Return the string excluding the suffix
        return text_string[:-len(suffix)]
    
    # If suffix doesn't match, return the original string
    return text_string


if __name__ == "__main__":
    # Suffix Testing
    name = 'lokendra'
    suffix_to_remove = 'dra'
    
    print(f"Original: '{name}'")
    print(f"After removing suffix '{suffix_to_remove}': '{custom_removesuffix(name, suffix_to_remove)}'")
    
    # Another test case
    file_name = 'script.py'
    ext = '.py'
    print(f"Original: '{file_name}'")
    print(f"After removing suffix '{ext}': '{custom_removesuffix(file_name, ext)}'")
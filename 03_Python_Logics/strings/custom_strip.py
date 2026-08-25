def custom_strip(text_string):
    """
    Removes leading and trailing whitespace from a given string.

    This function simulates the behavior of Python's built-in string method `.strip()`.
    It uses two index pointers to find the first and last non-space characters
    in the string, and then slices the string to remove all surrounding spaces.

    Args:
        text_string (str): The input string containing leading and/or trailing spaces.

    Returns:
        str: The stripped string without leading and trailing whitespace.

    Examples:
        >>> custom_strip('    lokendra    ')
        'lokendra'
        >>> custom_strip('   hello world   ')
        'hello world'
    """
    # Find the end index of the trimmed string
    end_index = len(text_string) - 1
    while end_index >= 0 and text_string[end_index] == ' ':
        end_index -= 1

    # Find the start index of the trimmed string
    start_index = 0
    while start_index < len(text_string) and text_string[start_index] == ' ':
        start_index += 1

    # Slice the string between the identified non-space boundaries
    return text_string[start_index:end_index + 1]


if __name__ == "__main__":
    text = '    lokendra    '
    stripped_text = custom_strip(text)
    
    print(f"Original: '{text}' (Length: {len(text)})")
    print(f"Stripped: '{stripped_text}' (Length: {len(stripped_text)})")
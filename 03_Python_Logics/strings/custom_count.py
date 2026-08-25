def count_character(text_string, target_char):
    """
    Counts the occurrences of a specific character in a given string.

    This function demonstrates the underlying logic of Python's built-in 
    string method `.count()`. It iterates through each character in the 
    string and increments a counter whenever a match with the target 
    character is found.

    Args:
        text_string (str): The string to search through.
        target_char (str): The character to count in the string.

    Returns:
        int: The number of times the target_char appears in the text_string.

    Examples:
        >>> count_character('Lokendra', 'k')
        1
        >>> count_character('banana', 'a')
        3
    """
    count_char = 0
    for i in text_string:
        if i == target_char:
            count_char += 1

    return count_char

if __name__ == "__main__":
    string = 'Lokendra'
    char = 'k'
    result = count_character(string, char)
    print(f"The character '{char}' appears {result} times in '{string}'.")
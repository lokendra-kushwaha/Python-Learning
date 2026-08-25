def custom_replace(text_string, old_substring, new_substring):
    """
    Replaces occurrences of a specified substring with a new substring.

    This function demonstrates the logic behind Python's built-in string 
    method `.replace()`. It iterates through the original string using a 
    while loop and slicing. If a match for the old substring is found, it 
    appends the new substring to the result and skips the appropriate 
    number of characters. Otherwise, it just appends the current character.

    Args:
        text_string (str): The original string to be modified.
        old_substring (str): The substring you want to find and replace.
        new_substring (str): The substring you want to insert instead.

    Returns:
        str: A new string with the replacements applied.

    Examples:
        >>> custom_replace('lokendra', 'dra', 'xyz')
        'lokenxyz'
        >>> custom_replace('hello world world', 'world', 'python')
        'hello python python'
    """
    result = ""
    i = 0
    
    # Iterate through the string using a while loop
    while i < len(text_string):
        # Check if the slice matches the old_substring
        if text_string[i:i + len(old_substring)] == old_substring:
            result += new_substring
            i += len(old_substring)  # Skip past the matched word
        else:
            result += text_string[i]
            i += 1  # Move to the next character
            
    return result


if __name__ == "__main__":
    text = "lokendra"
    old_word = 'dra'
    new_word = 'xyz'
    
    result = custom_replace(text, old_word, new_word)
    
    print(f"Original text: '{text}'")
    print(f"After replacing '{old_word}' with '{new_word}': '{result}'")
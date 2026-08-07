def find_character(string, target):
    """
    Decodes Python's built-in find() function for strings.

    Logic:
        Uses a for loop with enumerate() to iterate through the string and its indices. 
        It checks each character against the target and immediately returns the index 
        upon finding the first match, ensuring O(N) time complexity.

    Args:
        string (str): The main string to be searched.
        target (str): The target character that the user wants to locate.

    Returns:
        int: The index position of the first occurrence of the target character. 
             Returns -1 if the character is not found.
    """
    for index, char in enumerate(string):
        if char == target:
            return index

    return -1

if __name__ == "__main__":
    # Testing find_character function
    text1 = 'lokendra'
    search_char = 'r'
    print(f"Index of '{search_char}' in '{text1}':", find_character(text1, search_char))



string = 'lokendra'
target = 'r'

# Another method ------------------->
for i in range(len(string)):
    if string[i] == target:
        print(i)
        break
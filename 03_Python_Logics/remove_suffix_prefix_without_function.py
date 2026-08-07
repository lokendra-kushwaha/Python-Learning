def remove_custom_prefix(string, prefix):
    """
    Removes a specified prefix from a string if it exists.

    Logic:
        Checks if the beginning of the string matches the prefix using string slicing.
        If it matches, it returns the string from the end of the prefix to the last character.
        Otherwise, it returns the original string.

    Args:
        string (str): The original string.
        prefix (str): The prefix to be removed.

    Returns:
        str: The modified string without the prefix, or the original string if the prefix wasn't found.
    """
    if string[:len(prefix)] == prefix:
        return string[len(prefix):]
    else:
        return string


def remove_custom_suffix(string, suffix):
    """
    Removes a specified suffix from a string if it exists.

    Logic:
        Checks if the end of the string matches the suffix using negative string slicing.
        If it matches, it returns the string from the beginning up to the start of the suffix.
        Otherwise, it returns the original string.

    Args:
        string (str): The original string.
        suffix (str): The suffix to be removed.

    Returns:
        str: The modified string without the suffix, or the original string if the suffix wasn't found.
    """
    if string[-len(suffix):] == suffix:
        return string[0 : -len(suffix)]
    else:
        return string


if __name__ == "__main__":
    # Prefix Testing
    name1 = 'lokendra'
    prefix_to_remove = 'lo'
    print("After prefix removal:", remove_custom_prefix(name1, prefix_to_remove))

    # Suffix Testing
    name2 = 'lokendra'
    suffix_to_remove = 'dra'
    print("After suffix removal:", remove_custom_suffix(name2, suffix_to_remove))
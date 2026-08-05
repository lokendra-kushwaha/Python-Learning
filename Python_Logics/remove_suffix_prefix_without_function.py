"""
A program that decodes python in-built function removeprefix() function.
Input: A target substring (prefix) that user wants to remove from the starting of the string.
Execution: Checks if the string starts with the exact target substring using positive indexing and slicing. If a match is found, it slices off the prefix.
Output: Return the modified string (or the original string if the prefix is not found).
"""
string = 'lokendra'
prefix_remove = 'lo'

if string[:len(prefix_remove)] == prefix_remove:
    result = string[len(prefix_remove):]

else:
    result = string

print(result)

"""
A program that decodes python in-built function removesuffix() function.
Input: A target substring (suffix) that user wants to remove from the end of the string.
Execution: Checks if the string ends with the exact target substring using negative indexing and slicing. If a match is found, it slices off the suffix.
Output: Return the modified string (or the original string if the suffix is not found).
"""
string = 'lokendra'
suffix_remove = 'dra'

if string[-len(suffix_remove):] == suffix_remove:
    result = string[0 : -len(suffix_remove)]

else:
    result = string

print(result)
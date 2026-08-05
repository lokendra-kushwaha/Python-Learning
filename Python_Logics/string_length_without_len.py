"""
A program that calculates the lenght of string without using Python's buitt-in len() function.
Input - A standard string.
Execution: Initializes a counter variable to 0. A for loop iterates through the string character by character, incrementing the counter by 1 for every iteration.
Output: Returns the total length of the string as an integer.
"""

string = 'Lokendra Kushwaha'

string_length = 0
for char in string:
    string_length = string_length + 1

print(string_length)
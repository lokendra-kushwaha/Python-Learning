"""
This program calculates the lenght of string without string's buitt-in funnction len()
Input - Takes a strings
Execution: In the start assume string length is 0 and a for loop iterets charactor one by one and for one iteretion 1 increase in string length.
Output: Gives strings total lenth in integer.
"""

string = 'Lokendra Kushwaha'

string_length = 0
for char in string:
    string_length = string_length + 1

print(string_length)
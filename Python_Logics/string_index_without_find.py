"""
A program that decodes Python's built-in find() function for strings.
Input: A target character that the user wants to locate within a string.
Execution: Uses a for loop with enumerate() to iterate through the string and its indices. It checks each charcter against the target and breaks the loop immediately upon finding the match to ensure O(N) time complexity.
Output: Prints the index position (integer) of the first occurence of the target character.
"""
string = 'lokendra'
find_index = 'r'

for index, char in enumerate(string):
    if char == find_index:
        print(index)
        break

# Another method ------------------->
for i in range(len(string)):
    if string[i] == find_index:
        print(i)
        break
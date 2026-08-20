"""
Topic: For Loop Variations and Iteration
Goal: To practice iterating over strings, lists, using the range() function with step values, and nested loops.
"""

#==================================================================================================
#                                   for loop Practice   
#==================================================================================================

# 1. Iterating through a string character by character with a conditional check
name = "Lokendra Kushwaha"

for char in name:
    print(char)
    if(char == "L"):
        print("Hey, How Are You!")

#-------------------------------------------------------------
# 2. Using range() with start, stop, and step arguments 
# (Starts at 6, jumps by 4, and stops before 19)
for count in range(6, 19, 4):
    print(count)

#-------------------------------------------------------------
# 3. Nested Loops: 
# Outer loop picks each word from the list, inner loop prints each character of that word
colors = ["Yellow", "Purple", "Red", "Green"]

for color in colors:
    print(color)

    for i in color:
        print(i)

#-------------------------------------------------------------
# 4. Large range iteration to test loop execution speed
for k in range(20000):
    print(k)
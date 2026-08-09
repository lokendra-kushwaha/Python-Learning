"""
=============================================================================
Day 6: Strings in Python
=============================================================================
This module covers string creation, indexing, slicing, immutability, 
built-in string operations/methods, and practical algorithm building 
without using built-in functions.
"""

# ---------------------------------------------------------
# 1. CREATING STRINGS
# ---------------------------------------------------------
# In Python, strings are a sequence of Unicode Characters.

s1 = 'Hello'
s2 = "Hello World"
s3 = """Hello World""" # Used for multiline strings or docstrings

# Handling apostrophes inside strings:
# s4 = 'It's raining outside' # Throws a SyntaxError
s4 = "It's raining outside"     # Correct way

# Type casting to string
s_cast = str('hello')
print("String creations:", s1, s2, s3, s4)


# ---------------------------------------------------------
# 2. ACCESSING SUBSTRINGS (INDEXING & SLICING)
# ---------------------------------------------------------
s = 'Hello World'

# --- Indexing ---
print("\n--- Indexing ---")
print("Positive Indexing (First char):", s[0])
print("Negative Indexing (4th from last):", s[-4])

# --- Slicing [start:stop:step] ---
print("\n--- Slicing ---")
print("Extract index 1 to 4:", s[1:5])
print("Extract index 1 to end:", s[1:])
print("Extract from start to 5 with step 3:", s[0:6:3])
print("Reverse string (Idiomatic):", s[::-1])
print("Negative slicing (last 5 chars):", s[-5:])
print("Negative slicing in reverse:", s[-1:-6:-1])


# ---------------------------------------------------------
# 3. EDITING & DELETING (IMMUTABILITY)
# ---------------------------------------------------------
# Python strings are IMMUTABLE (cannot be modified after creation).

s = 'Hello World'
# s[0] = 'h' # Throws TypeError: 'str' object does not support item assignment

# You cannot delete parts of a string either:
# del s[-1:-5:2] # Throws TypeError

# You can only delete the entire string object from memory:
del s 


# ---------------------------------------------------------
# 4. STRING OPERATIONS
# ---------------------------------------------------------
print("\n--- String Operations ---")

# --- Arithmetic Operations (+, *) ---
print("Concatenation:", 'delhi' + 'mumbai') 
print("Repetition:", 'delhi ' * 5) 
print('=' * 30) # Prints a divider line

# --- Relational Operators ---
# Compares lexicographically (based on ASCII values)
print("Is 'delhi' == 'mumbai'?", 'delhi' == 'mumbai')
print("Is 'mumbai' > 'pune'?", 'mumbai' > 'pune') # False ('m' is smaller than 'p')
print("Is 'Pune' > 'pune'?", 'Pune' > 'pune')     # False ('P' is 80, 'p' is 112 in ASCII)

# --- Logical Operators ---
# Empty strings '' evaluate to False. Non-empty strings evaluate to True.
print("Empty AND 'world':", '' and 'world')       # Returns '' (False)
print("Empty OR 'world':", '' or 'world')         # Returns 'world' (True)
print("Logical NOT empty:", not '')               # True

# --- Membership Operators ---
print("Is 'D' in 'Delhi'?", 'D' in 'Delhi')           # True
print("Is 'D' not in 'delhi'?", 'D' not in 'delhi')   # True


# ---------------------------------------------------------
# 5. COMMON FUNCTIONS & METHODS
# ---------------------------------------------------------
print("\n--- Built-in Functions ---")
test_str = 'hello world'
print("Length:", len(test_str))
print("Max Char (ASCII):", max(test_str))
print("Min Char (ASCII):", min(test_str))
print("Sorted (Returns List):", sorted(test_str))

print("\n--- Case Formatting Methods ---")
print("Capitalize:", test_str.capitalize())
print("Title:", test_str.title())
print("Upper:", test_str.upper())
print("Swapcase:", test_str.swapcase())

print("\n--- Searching & Counting ---")
target = 'My name is lokendra'
print("Count 'a':", target.count('a')) 
print("Find 'is':", target.find('is'))
print("Find 'z' (Not found):", target.find('z')) # Returns -1 safely
# print("Index 'z':", target.index('z'))         # Throws ValueError if not found

print("\n--- Formatting ---")
name = 'lokendra'
gender = 'male'
print('Hi my name is {} and I am a {}.'.format(name, gender))
print('Hi my name is {1} and I am a {0}.'.format(gender, name)) # Using positional indices

# --- String Validation (Boolean Methods) ---
print("\n--- String Validation (Boolean Methods) ---")

# isalnum(): Checks if all characters are alphabets or numbers (no special chars)
print("Is 'lokendra1234' Alphanumeric?:", 'lokendra1234'.isalnum()) 
print("Is 'lokendra1234%' Alphanumeric?:", 'lokendra1234%'.isalnum()) # False due to '%'

# isalpha(): Checks if all characters are only alphabets
print("Is 'lokendra' Alphabetic?:", 'lokendra'.isalpha())

# isdigit(): Checks if all characters are only numbers
print("Is '1234' Digit?:", '1234'.isdigit())

# isidentifier(): Checks if the string can be used as a valid variable name in Python
print("Is 'lokendra_' a valid Identifier?:", 'lokendra_'.isidentifier())

print("\n--- Splitting, Joining, Replacing, Stripping ---")
s_split = 'Hi my name is lokendra'
print("Split:", s_split.split())
print("Join:", ' '.join(['Hi', 'my', 'name', 'is', 'lokendra']))
print("Replace:", s_split.replace('lokendra', 'vivek'))
print("Strip (removes padding):", '   lokendra   '.strip())


# ---------------------------------------------------------
# 6. PRACTICAL STRING PROGRAMS (Algorithm Building)
# ---------------------------------------------------------

# Program 1: Finding length without len() function
string_1 = 'lokendra'
count = 0
for char in string_1:
    count += 1
print("\nLength without len():", count)

# Program 2: Extracting username from email (Two Methods)
email = 'lokendrakushwaha@gmail.com'
print("Username (Method 1 - Split):", email.split('@')[0])
print("Username (Method 2 - Slicing):", email[0:email.index('@')])

# Program 3: Check if string is a palindrome
pal_string = "radar"
if pal_string == pal_string[::-1]:
    print(f"'{pal_string}' is a palindrome string.")

# Program 4: Split a string without using split() method
raw_string = "Hello world this is Python"
l = []
temp = ''
for i in raw_string:
    if i != ' ':
        temp = temp + i
    else:
        l.append(temp)
        temp = ''
l.append(temp) # Append the last word 
print("Custom split result:", l)

# Program 5: Convert string to Title Case without title() function
title_target = "lokendra is learning python"
new_string = []
for i in title_target.split():
    new_string.append(i[0].upper() + i[1:].lower())
print("Custom title case:", ' '.join(new_string))

# Program 6: Convert integer to string format without str()
number = 4567
digits = '0123456789'
result = ''
while number != 0:
    result = digits[number % 10] + result
    number = number // 10
print("Int to String format:", result)

# Program 3: Count frequency of a character (Custom Logic)
s_input = input("\nEnter your email: ")
char_to_search = input("What character would you like to search: ")
counter = 0
for i in s_input:
    if i == char_to_search:
        counter += 1
print(f"Frequency of '{char_to_search}':", counter)

# Program 4: Remove a particular character from a string
string_target = input("\nEnter the string: ")
term = input("What character would you like to remove: ")
result = ''
for i in string_target:
    if i != term:
        result += i
print("String after removal:", result)

# Program 5 (Method 2): Palindrome check using Loop & Flag (Without Slicing)
string_pal = input("\nEnter a string to check palindrome: ")
flag = True
# Loop runs only till the half length of the string
for i in range(0, len(string_pal) // 2):
    # Comparing first character with last, second with second-last...
    if string_pal[i] != string_pal[len(string_pal) - i - 1]:
        print("Not a palindrome (Checked via loop)")
        flag = False
        break

if flag:
    print("Palindrome (Checked via loop)")
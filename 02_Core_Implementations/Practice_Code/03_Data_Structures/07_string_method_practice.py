"""
String Methods Practice & Cheat Sheet
-------------------------------------
A collection of Python's built-in string methods.
Used for quick reference and understanding string manipulation.
"""

# --- 1. Basic Case Conversions ---
a = "hey lokendra!"
print("Original:", a)
print("Upper:", a.upper())

a = "HOW are you?"
print("Lower:", a.lower())


# --- 2. Stripping Whitespaces & Characters ---
a = "       I want to eat food.         "
print("Original:", a)
print("Strip (removes spaces from ends):", a.strip())

a = "I am learning Pythonnnn"
print("Rstrip (removes 'n' from right):", a.rstrip("n"))


# --- 3. Replacing & Splitting ---
a = "I am a bad boy."
print("Replace:", a.replace("bad", "good"))

a = "Samosa FrenchFries CocaCola Cake"
print("Split (creates a list):", a.split(" "))


# --- 4. Advanced Case Formatting ---
a = "i am a rich man and he ia a poor man."
print("Capitalize (first letter only):", a.capitalize())

a = "How are You?"
print("Swapcase (inverts cases):", a.swapcase())

a = "international monetary fund"
print("Title (capitalizes every word):", a.title())


# --- 5. Alignment & Padding ---
a = "Hey Donkey!"
print("Center (with spaces):", a.center(100))
print("Center (with custom char):", a.center(100, "#"))


# --- 6. Searching & Counting ---
a = "Banana"
print("Count of 'n':", a.count("n"))

a = "I love you..."
print("Ends with '...':", a.endswith("..."))

a = "Lokendra is a very good man."
print("Starts with 'Lokendra':", a.startswith("Lokendra"))

a = "I hate you..."
print("Find 'hate' (returns index):", a.find("hate"))
print("Find 'love' (returns -1 if not found):", a.find("love"))

a = "His name is Jack. Jack is a handsome man."
print("Index of 'Jack':", a.index("Jack"))


# --- 7. String Validation (Boolean Checks) ---
a = "HeHas20Rupees"
print("Is Alpha-Numeric:", a.isalnum())

a = "HeHasTwentyRupees"
print("Is Alphabetic only:", a.isalpha())

a = "my name is lokendra"
print("Is strictly Lowercase:", a.islower())

a = "MY NAME IS LOKENDRA"
print("Is strictly Uppercase:", a.isupper())

a = "Hey Shri!"
print("Is Printable:", a.isprintable())

a = "    "
print("Is Space (4 spaces):", a.isspace())

a = "       "
print("Is Space (7 spaces):", a.isspace())

a = "Welcome To The Hell"
print("Is Title Case:", a.istitle())
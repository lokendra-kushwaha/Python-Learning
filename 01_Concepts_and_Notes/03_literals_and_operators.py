"""
=============================================================================
Day 3: Literals and Operators
=============================================================================
This module covers literals (the actual data values stored in variables), 
all major Python operators, and a practical digit-sum algorithm.
"""

# ---------------------------------------------------------
# 1. LITERALS
# ---------------------------------------------------------
# A literal is the raw data assigned to a variable.

# --- Numeric Literals ---
a = 0b1010       # Binary Literal (Prefix: 0b)
b = 100          # Decimal Literal
c = 0o310        # Octal Literal (Prefix: 0o)
d = 0x12c        # Hexadecimal Literal (Prefix: 0x)
print("Numeric Literals:", a, b, c, d)

# --- Float Literals ---
float_1 = 10.5
float_2 = 1.5e2  # Scientific notation (1.5 * 10^2 = 150.0)
float_3 = 1.5e-3 # Scientific notation (1.5 * 10^-3 = 0.0015)
print("Float Literals:", float_1, float_2, float_3)

# --- Complex Literals ---
x = 3 + 3.14j    # Real part = 3.0, Imaginary part = 3.14
print("Complex Literals:", x, "| Imaginary:", x.imag, "| Real:", x.real)

# --- String Literals ---
string_sq = 'This is Python'          # Single quotes
string_dq = "This is Python"          # Double quotes
char = 'C'                            # Single character
multiline_str = """The 
Lokendra"""                           # Triple quotes for multiline strings
unicode_str = u"\U0001f600\U0001F606" # Unicode (Emojis)
raw_str = r"raw \n string"            # Raw string (ignores escape sequences like \n)
print("Strings:", string_sq, char, unicode_str, raw_str)

# --- Boolean Literals ---
# In Python, True behaves like integer 1, and False behaves like integer 0 in math.
bool_1 = True + 4   # 1 + 4 = 5
bool_2 = False + 10 # 0 + 10 = 10
print("Boolean Math:", bool_1, bool_2)

# --- Special Literal (None) ---
# Used to define a variable whose value will be assigned later.
a = None
b = 6
# print(a + b)  # This would throw a TypeError because you can't add None to an integer.

# Correct way to use it:
a = None  # Placeholder
a = 4     # Value assigned later
b = 5
print("None usage result:", a + b)


# ---------------------------------------------------------
# 2. OPERATORS
# ---------------------------------------------------------

# --- 1. Arithmetic Operators ---
print("Addition:", 5 + 4)
print("Subtraction:", 5 - 4)
print("Multiplication:", 5 * 4)
print("Division (Float):", 5 / 4)
print("Floor Division (Int):", 5 // 4)
print("Modulus (Remainder):", 5 % 4)
print("Exponent (Power):", 5 ** 2)

# --- 2. Relational (Comparison) Operators ---
print("Greater than:", 4 > 5) 
print("Equal to:", 4 == 5)
print("Less than or equal to:", 4 <= 5)
print("Not equal to:", 4 != 5)

# --- 3. Logical Operators ---
# 'and' evaluates to True ONLY if both operands are True.
# 'or' evaluates to True if AT LEAST ONE operand is True.
print("Logical AND:", 1 and 0) 
print("Logical OR:", 1 or 0)   
print("Logical NOT:", not 0)   

# --- 4. Bitwise Operators (Operates on binary level) ---
print("Bitwise AND:", 2 & 3)
print("Bitwise OR:", 2 | 3)
print("Bitwise XOR:", 2 ^ 3)   # 1 if bits are different, 0 if same
print("Bitwise NOT:", ~3)
print("Bitwise RIGHT Shift:", 4 >> 2) # >> Shifts bits to the right
print("Bitwise LEFT Shift:", 5 << 2)  # << Shifts bits to the left

# --- 5. Assignment Operators ---
var_a = 2     # '=' is the standard assignment
var_a += 2    # Equivalent to: var_a = var_a + 2
print("Assignment (+=):", var_a)

# --- 6. Membership Operators ---
# Checks if an element exists in a sequence (string, list, tuple, etc.)
print("Is 'D' in 'Delhi'?", 'D' in 'Delhi')           # True
print("Is 'D' not in 'Delhi'?", 'D' not in 'Delhi')   # False
print("Is 1 in [2, 3, 4, 5, 6]?", 1 in [2, 3, 4, 5, 6]) # False


# ---------------------------------------------------------
# 3. PRACTICAL PROGRAM: Sum of a 3-Digit Number
# ---------------------------------------------------------
# Extracting individual digits using Modulus (%) and Floor Division (//).

number = int(input("\nEnter a 3-digit number: "))

# Extract last digit
a = number % 10
number = number // 10

# Extract middle digit
b = number % 10
number = number // 10

# Extract first digit
c = number % 10

print(f"The sum of the digits is: {a + b + c}")
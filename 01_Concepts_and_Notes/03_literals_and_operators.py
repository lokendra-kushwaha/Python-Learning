#==================================================================================================
#                              Day - 3 : Literals
#==================================================================================================

# <--- Literals --->
# The value stored in variable called literals.

# 1. Interger Literals -->
a = 0b1010 # Binary Literals 
# a --> Variable , = --> Operator, 0b1010 -- > Literal
b = 100 # Decimal Literal
c = 0o310 # Octal Literal
d = 0x12c # Hexadecimal Literal
print(a, b, c, d)

# 2. Float Literals
float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e-3
print(float_1, float_2, float_3)

# 3. Complex Literals
x = 3 + 3.14j
print(x, x.imag, x.real)

# 4. Strings
strings = 'This is Python' # String in single quote also valid .
strings = "This is Python" # String in double quote also valid.
char = 'C' # Single character also valid
multiline_str = """The 
Lokendra""" # Multiline string written in triple inverted commas.

unicode = u"\U0001f600\U0001F606\U0001F923"
raw_srt = r"raw \n string"
print(strings, strings, char, unicode, multiline_str, raw_srt)

a = True + 4 # Bollen data type treated by python as 0 or 1.
b = False + 10
print(a, b)

a = None
print(a)

# k # throws an error # We can'not write a varible name without literal.
b = 6
c = 4
print(a+b)
# For solve this problem

a = None # Now we can define this variable leter.
b = 4
c = 5
print(b + c)

# <--- Operators --->

# Operators in Python -->

# 1. Arithmetic Operators
print(5+4) # Addition 
print(5-4) # Substraction
print(5*4) # Multiply
print(5/4) # Divide
print(5//4) # Floor division/integer division
print(5%4) # Modulus operator --> tells reminder
print(5**2) # Power of operator

# 2. Relational Operators
# Compares two quantities.
print(4 > 5) 
print(4 == 5)
print(4 <= 5)
print(4 != 5)

# 3. Logical Operators
# 1. and 2. or 3. not

print(1 and 0) # jb dono 1 honge tabhi and ka output 1 hoga else vice versa
print(1 or 0) # jb ek true hota h to vahi output hota h
print(not 0) # Reverse 

# 4. Bitwise Operators --> Operated on binary values

# bitwise and operator
print(2 & 3)

# bitwise or operator 
print(2 | 3)

# bitwise xor operator
print(2 ^ 3) # for same binary base 0 and where is different then 0

# bitwise not operator
print(~ 3)

# bitwide left shift
print(4 >> 2)

# bitwise right shift
print(5 << 2)

# 5. Assignment Operator
a = 2
# = --> Assignment operator

a = 2
a += 2 # means --> a = a + 2
print(a)

# 5. Membership Operators

# 1. in 2. not in

print('D' in 'Delhi') # Output --> True
print('D' not in 'Delhi') # Output --> False

print(1 in [2, 3, 4, 5, 6]) # Output --> False because 1 is not exists in list.

# Program - Find the sum of a 3 digit number entered by user

number = int(input("Enter a 3 digit number: "))
a = number%10
number = number//10

b = number%10
number = number//10

c = number%10

print(a + b + c)
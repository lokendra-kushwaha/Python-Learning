"""
                            Here's my Python Learning Journey
"""
#==================================================================================================
#           Day - 1 : Print Statements, Comments & Escape Sequences
#==================================================================================================

# <--- About Print --->
# For print a datatype like Integer, float or String in console we use python's in-bulit function that is 'Print()'.

print("Lokendra Kushwaha", end=' ') # end parameter: Romoves default \n character after print.
print("is Male")

print('I', 'am', 'a', 'developer.', sep='*') # sep parameter: Defines the character between multiple argumets which is space by default.

# <--- Comments --->
# Piece of code and ignored by python interpreter.

# This is my first program --> Commented line
print("Hello World!")

# <--- Escape Sequences --->

print("He said, \"I want to eat.\"") # Or
print('He said, "I want to eat."')
print("He is a \"good boy\" \nand she is also a \"good girl.\"")

#==================================================================================================
#                              Day - 2 : Datatypes And Variables
#==================================================================================================

# <--- Data type --->

print(1e308) # Max integer number that can handeled by python interpreter
print(1.7e308) # Max float number that can handeled by python interpreter
print(True) # Boolean datatype
print(False) # Boolean datatype
print("lokendra") # String datatype
print(5+6j) # A complex number

# Python -> List -> C -> Array
print([1, 2, 3]) # (In C language python's list called Arrey)
print((1, 2, 3)) # Tuple
print({1, 2, 3}) # Set datatype
print({1:2, 3:4}) # Dictionary datatype

print(type(3)) # We can check any item's datatype by using python's in-built function called type()

# <--- Variables ---> Variables are the containers for future use.
name = 'nitesh'
print(name)

a = 5
b = 6
print(a + b)

# Dynamic typing
a = 5 # Where you do not tell datatype to variable called dynamic typing.

# Static typing 
# int a = 5 # In C variable decalres such as and also Java supports stating typing.

# Dynamic Binding
a = 5
print(a)

a = 'nitesh'
print(a)

# Static binding --> Used in C and C++ and Java
# int a = 5 # Now in all programm a can olny store int datatype.

#------------------
a = 1
b = 2
c = 3
print(a, b, c)

a, b, c = 1, 2, 3
print(a, b, c)

a = b = c = 5
print(a, b, c)
#-------------------

# <--- Keywords and Identifiers --->

# Keywords --> In python 32 keywords exists
# ex. if, else, elif, return, True, False, yield etc.

# Compiler --> pure code ko ak sath low level language me convert krta h ex. c, java
# Interpreted --> line by line code ko low level language me convert krta h ex. python, javascript

# Identifiers -->
# 1. You can not start with a digit

# 1name = 'nitesh' # Throws an error
name1 = 'nitesh' # Would work

# 2. You can use specials character only '_' others not allowed ex. %, $

# first-name = 'lokendra' # throws an error
first_name = 'lokendra' # Would work

_ = 'lokendra'
print(_)

# 3. Identifiers can not be keywords.

# User Input -->

# Static software -> jo user se bat nhi krte ex. calender, clock, blog, college website.
# Dynamic software -> jo user se bat krte h ex. youtube, zomato etc.

# Take input from users and store them in a variable.
fnum = input("Enter first number ")
snum = input("Enter second number: ")
# Add the 2 variables
add = int(fnum) + int(snum)
# Print the result
print(add)
print(type(fnum)) # Python's type conversion operation does not changes the original data it's create a new value

# Type Conversion -->

# Two types.- 1. Implicit 2. Explicit

print(5 + 5.6) # Implicite type conversion (It is done by python interpreter.)
print(type(5), type(5.6))

print(4 + '4') # Explicit type --> In python there are built in functions for type conversion.

print(int('4'))

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

# <--- Operators + if else + Loops --->

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

# <--- if else in Python --> 
# For handaling branching in program.

# login program and indentation
# email --> nitesh.campusx@gmail.com, password --> 12345

email = input("Enter your email: ")
password = input("Enter your password: ")

if email == 'nitesh.campusx@gmail.com' and password == '12345':
    print("Welcome")

elif email == 'nitesh.campusx@gmail.com' and password != '12345':
    print("Please enter correct password.")

    password = input("Enter password again: ")
    if password == '12345':
        print("Welcome")

    else:
        print("beta tumse na ho payega.")

else:
    print("Chl nikal.")

# Find the min of 3 numbers.

a = int(input("First num: "))
b = int(input("Second num: "))
c = int(input("Third num: "))

if a < b and a < c:
    print('smallest is', a)

elif b < c:
    print('smallest is', b)

else:
    print('smallest is', c)

# Calculator

fnum = int(input("Enter the first num: "))
snum = int(input("Enter the second num: "))

op = input('Enter the operation: ')

if op == '+':
    print(fnum + snum)

elif op == '-':
    print(fnum - snum)

elif op == '*':
    print(fnum * snum)

else:
    print(fnum/snum)

# Menu driven calculator

menu = input("""
Hii! How i can help you.
1. Enter 1 for pin change
2. Enter 2 for balance check
3. Enter 3 for withdrawl
4. Enter 4 for exit
""")

if menu == '1':
    print("pin change")

elif menu == '2':
    print("balance check")

elif menu == '3':
    print("withdrawl")

else:
    print('exit')

# Modules in python -->
# Ex.-- # math # keywords # random # datetime

# 1. math module
import math

print(math.factorial(5))
print(math.floor(6.8))
print(math.sqrt(25))

# 2. keyword module
import keyword

print(keyword.kwlist)

# 3.random module
import random

print(random.randint(0, 100))

# 4. datetime module
import datetime

print(datetime.datetime.now())

print(help('modules')) # Prints all modules that exists in python
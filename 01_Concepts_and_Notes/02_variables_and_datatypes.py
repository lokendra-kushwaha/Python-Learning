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
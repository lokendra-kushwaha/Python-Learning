#==================================================================================================
#                           Day - 4 : If-else and Match Case Statements
#=================================================================================================

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

# Match case statements in python -->

x = int(input("Enter your number : "))
# x is the variable to match
match x:
    # if x ix 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x != 90: # _ means case is exeptional
        print(x, "is not 90")

    case _ if x != 80:
        print(x, "is not 80")
    case _:
        print(x)

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
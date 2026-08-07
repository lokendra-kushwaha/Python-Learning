"""
Topic: Arithmetic Operators and Type Casting
Goal: To practice basic mathematical operations and understand the difference between integer math and string concatenation.
"""

#==================================================================================================
#                          Calculation on two numbers using arithmetic operators
#==================================================================================================

x = 10
y = 6
print(x, "+", y, "=", x + y)
print(x, "-", y, "=", x - y)
print(x, "x", y, "=", x * y)
print(x, "/", y, "=", x / y)
print(x, "//", y, "=", x // y, "(Floor Division)")
print(x, "%", y, "=", x % y, "(Modulus)")

#==================================================================================================
# Interactive calculation: Demonstrating type casting (int to str) and mathematical operations.
#==================================================================================================

# Taking user input and converting it to integers
n1 = int(input("Enter Your First No. : "))
n2 = int(input("Enter Your Second No. : "))

# 1. Addition
x = input("For the Sum of First Number and Second Number Enter + : ")
# Using str() to show concatenation vs integer addition
print("The String of", n1, "and", n2, "is", str(n1)+str(n2))
print("The Sum of", n1, "and", n2, "is", n1+n2)

# 2. Subtraction
x = input("For the Substraction of First Number and Second Number Enter - : ")
print("The String of", n1, "and", n2, "is", str(n1)+str(n2))
print("The Sum of", n1, "and", n2, "is", n1-n2)

# 3. Multiplication
x = input("For the Multiplication of First Number and Second Number Enter x : ")
print("The String of", n1, "and", n2, "is", str(n1)+str(n2))
print("The Sum of", n1, "and", n2, "is", n1*n2)

# 4. Division
x = input("For the Divide of First Number and Second Number Enter / : ")
print("The String of", n1, "and", n2, "is", str(n1)+str(n2))
print("The Sum of", n1, "and", n2, "is", n1/n2)

# 5. Exponential (Power)
x = input("For the Exponential of First Number and Second Number Enter ^ : ")
print("The String of", n1, "and", n2, "is", str(n1)+str(n2))
print("The Sum of", n1, "and", n2, "is", n1**n2)

# 6. Modulus (Remainder)
x = input("For the Module of First Number and Second Number Enter % : ")
print("The String of", n1, "and", n2, "is", str(n1)+str(n2))
print("The Sum of", n1, "and", n2, "is", n1%n2)

# 7. Floor Division
x = input("For the Floor Division of First Number and Second Number Enter // : ")
print("The String of", n1, "and", n2, "is", str(n1)+str(n2))
print("The Sum of", n1, "and", n2, "is", n1//n2)
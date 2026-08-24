# =====================================================================
# 🐍 Python Object-Oriented Programming (OOP) - Fundamentals
# =====================================================================

# ---------------------------------------------------------------------
# 1. Everything in Python is an Object
# ---------------------------------------------------------------------

# In Python, every data type (like list, string, integer) is fundamentally an object of a specific class. If you try to call a method that doesn't exist in that class, Python throws an error.

# python
# List Example
L = [1, 2, 3]
# L.upper() 
# ❌ AttributeError: 'list' object has no attribute 'upper'
# Reason: The 'list' class does not have any rule/method named 'upper'.

# String Example
s = 's'
# s.append('x') 
# ❌ AttributeError: 'str' object has no attribute 'append'
# Reason: The 'str' class does not possess the 'append' behavior.

# ---------------------------------------------------------------------
# 2. What is OOP?
# ---------------------------------------------------------------------

# OOP is a programming paradigm—a way of writing code—that allows us to create our own custom data types. It revolves around bundling data (attributes) and behavior (methods) into a single logical unit.
# The 6 Core Principles of OOP:
#  * Class
#  * Object
#  * Polymorphism
#  * Encapsulation
#  * Inheritance
#  * Abstraction

# ---------------------------------------------------------------------
# 3. Classes and Objects
# ---------------------------------------------------------------------

#  * Class: A blueprint or a set of rules that defines how an object will behave. It consists of:
#    * Data / Properties (Variables)
#    * Behaviors (Functions/Methods)
#    * Types of Classes: Built-in (e.g., list, str, set) and User-defined.
#  * Object: An instance of a class. When we assign a class to a variable, it becomes an object that can access the rules and properties defined inside that class.
# Syntax to create an object:
# object_name = ClassName()

# Example with built-in classes:
l = list() # Creating a list object
s = str()  # Creating a string object

# > 💡 Note: Python allows "object literals" for built-in types (like l = [1, 2, 3]), so we don't always have to instantiate them explicitly using parentheses.
 
# ---------------------------------------------------------------------
# 4. Methods vs Functions
# ---------------------------------------------------------------------

# Though they look similar, there is a fundamental architectural difference:
#  * Functions: Independent blocks of code that exist outside a class.
#  * Methods: Functions that are defined inside a class and can only be accessed by the object of that class.
l = [1, 2, 3]
print(len(l))  # len() is a Built-in Function (Independent)
l.append(4)    # append() is a Method (Belongs to the list class)

# ---------------------------------------------------------------------
# 5. The Golden Concept of 'self'
# ---------------------------------------------------------------------

# The Problem: The golden rule of OOP states that only an object can access the methods and data of its class. So, can one method inside a class call another method in the same class directly? No.
# The Solution (self): self acts as a bridge. It is essentially a reference to the current calling object. It allows methods within the same class to communicate with each other.
class Temp:
    def __init__(self):
        # Printing the memory address of the current object
        print("Address of self:", id(self))

obj = Temp()
print("Address of obj :", id(obj)) 
# Both will output the exact same memory address!

obj1 = Temp() 
print("Address of obj1:", id(obj1)) 
# This will have a different address, and 'self' will now point to obj1.

# > 💡 Pro-Tip: self is not a reserved keyword in Python. It's merely a strong convention. You could technically name it this or me, but standard Python PEP-8 guidelines strictly recommend using self.

# ---------------------------------------------------------------------
# 6. Magic / Dunder Methods & Constructor
# ---------------------------------------------------------------------

# Magic methods (also known as Dunder methods, short for "Double Underscore") are special methods that provide "superpowers" to your classes. They are invoked automatically under the hood by Python.
#  * Representation: __methodname__
# The Constructor: __init__
# The constructor is a special dunder method that is automatically executed the moment an object is instantiated. You do not need to call it explicitly.
# Why use a constructor?
# It is primarily used to write configuration-related code—code that must run before the user interacts with the object (e.g., connecting to a database, initializing variables, or fetching internet configurations). We don't want to rely on the user to manually call a setup function.

# =====================================================================
# 7. Project 1: ATM Machine Simulator
# =====================================================================

# Class Diagram
# (This will render as a visual diagram on GitHub)
# classDiagram
#     class Atm {
#         +string pin
#         +int balance
#         +__init__()
#         +menu()
#         +create_pin()
#         +change_pin()
#         +check_balance()
#         +withdraw()
#     }

# Python Implementation
# Note: Class names in Python follow PascalCase convention (e.g., AtmMachine).

class Atm:
    """A simple ATM Machine simulator showcasing OOP concepts."""

    def __init__(self):
        # Instance variables initialized
        self.pin = ''
        self.balance = 0
        # Automatically triggering the menu upon object creation
        self.menu()

    def menu(self):
        """Displays the main interface and handles user routing."""
        user_input = input("""
            How can I help you?
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check balance
            4. Press 4 to withdraw
            5. Anything else to exit
            --> """)
        
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            print("Exiting... Have a nice day!")
            exit()

        # Loop back to menu after an operation completes
        self.menu()

    def create_pin(self):
        self.pin = input('Enter your new pin: ')
        self.balance = int(input('Enter initial balance: '))
        print("✅ Pin created successfully!")

    def change_pin(self):
        old_pin = input("Enter old pin: ")
        if old_pin == self.pin:
            new_pin = input("Enter new pin: ")
            self.pin = new_pin
            print("✅ Pin changed successfully.")
        else:
            print("❌ Incorrect old pin.")

    def check_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            print(f"💰 Your current balance is ₹{self.balance}")
        else:
            print("❌ Incorrect pin.")

    def withdraw(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            amount = int(input("Enter the withdrawal amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"✅ Withdrawal successful. Remaining balance is ₹{self.balance}")
            else:
                print("❌ Insufficient balance.")
        else:
            print("❌ Incorrect pin.")

# Object creation
# sbi = Atm()
# print(type(sbi)) # Output: <class '__main__.Atm'>

# =====================================================================
# 8. Project 2: Creating a Custom Datatype (Fraction)
# =====================================================================
# Demonstrates Operator Overloading using magic methods.
# This project demonstrates Operator Overloading using magic methods. We are teaching Python how to add, subtract, multiply, and divide our newly invented custom datatype (Fraction).

class Fraction:
    """A custom datatype to handle mathematical fractions."""
    
    # Parameterized constructor expecting numerator (x) and denominator (y)
    def __init__(self, x, y):
        self.num = x
        self.den = y

    def __str__(self):
        """
        Superpower: Triggered when the object is passed into print().
        It dictates how the object should visually represent itself as a string.
        """
        return f"{self.num}/{self.den}"
    
    def __add__(self, other):
        """Defines the behavior of the '+' operator for Fraction objects."""
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __sub__(self, other):
        """Defines the behavior of the '-' operator."""
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __mul__(self, other):
        """Defines the behavior of the '*' operator."""
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        """Defines the behavior of the '/' operator."""
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)
    
    def convert_to_decimal(self):
        """A normal custom method to return the float value of the fraction."""
        return self.num / self.den

# Testing our custom datatype
fr1 = Fraction(1, 2)
fr2 = Fraction(3, 4)

print("Fraction 1:", fr1)               # Output: 1/2
print("Fraction 2:", fr2)               # Output: 3/4
print("Addition:", fr1 + fr2)           # Output: 10/8
print("Subtraction:", fr1 - fr2)        # Output: -2/8
print("Multiplication:", fr1 * fr2)     # Output: 3/8
print("Division:", fr1 / fr2)           # Output: 4/6
print("Decimal Form (fr1):", fr1.convert_to_decimal()) # Output: 0.5
"""
=========================================================
🧮 MATRIX OPERATIONS - VERSION 1.0 (2x2 HARDCODED) 🧮
=========================================================

Description:
    This is my very first attempt at building a Matrix class in Python.
    It strictly handles 2x2 matrices using hardcoded variables and 
    returns formatted strings for Addition, Subtraction, and Multiplication.

    (A stepping stone to the later n x n 2D-list dynamic matrix project!)

Created By: Lokendra Kushwaha
"""

from random import randint as element

class Matrix:
    def __init__(self):
        # Generating a random 2x2 matrix
        self.a11 = element(-10, 10)
        self.a12 = element(-10, 10)
        self.a21 = element(-10, 10)
        self.a22 = element(-10, 10)

    def __str__(self):
        return f"[{self.a11:^4} {self.a12:^4}]\n[{self.a21:^4} {self.a22:^4}]"
    
    def add(self, other):
        return f"[{self.a11 + other.a11:^4} {self.a12 + other.a12:^4}]\n[{self.a21 + other.a21:^4} {self.a22 + other.a22:^4}]"
    
    def sub(self, other):
        return f"[{self.a11 - other.a11:^4} {self.a12 - other.a12:^4}]\n[{self.a21 - other.a21:^4} {self.a22 - other.a22:^4}]"
    
    def mul(self, other):
        return f"[{self.a11*other.a11 + self.a12*other.a21:^4} {self.a11*other.a12 + self.a12*other.a22:^4}]\n[{self.a21*other.a11 + self.a22*other.a21:^4} {self.a21*other.a12 + self.a22*other.a22:^4}]"

def main():
    print("=" * 40)
    print("      🧮 MATRIX OPERATIONS (V1) 🧮      ")
    print("=" * 40)

    m1 = Matrix()
    m2 = Matrix()
    
    print("Matrix 1:")
    print(m1, '\n')
    
    print("Matrix 2:")
    print(m2, '\n')

    print("-" * 40)
    print("Addition (M1 + M2):")
    print(m1.add(m2), '\n')

    print("Subtraction (M1 - M2):")
    print(m1.sub(m2), '\n')

    print("Multiplication (M1 * M2):")
    print(m1.mul(m2))
    print("=" * 40)

if __name__ == "__main__":
    main()
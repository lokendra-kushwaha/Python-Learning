"""
=========================================================
🧮 QUADRATIC EQUATION SOLVER (OOP APPROACH) 🧮
=========================================================

Description:
    My early exploration into Object-Oriented Programming (OOP) in Python!
    This script defines a QuadraticEquation class to represent and solve 
    equations of the standard form ax^2 + bx + c = 0.

    It features a highly creative string-manipulation hack to format 
    the final mathematical factors perfectly.

Created By: Lokendra Kushwaha
"""

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        # Using standard mathematical representation
        return f"{self.a}x² + {self.b}x + {self.c} = 0"
    
    def fractionFactors(self):
        # Calculating the Discriminant (D)
        D = (self.b**2 - 4 * self.a * self.c)**0.5
        
        # The legendary string replacement hack for formatting!
        fac1 = f"({(self.a * 2)}x - {-self.b + D})".replace('- -', '+ ')
        fac2 = f"({(self.a * 2)}x - {-self.b - D})".replace('- -', '+ ')
        
        return fac1, fac2

def main():
    print("=" * 50)
    print("         🧮 QUADRATIC EQUATION SOLVER 🧮         ")
    print("=" * 50)
    
    # Testing the class with 2x^2 + 5x + 2 = 0
    ex = QuadraticEquation(2, 5, 2)
    
    print(f"Equation : {ex}")
    
    # Fetching the factors
    factors = ex.fractionFactors()
    print(f"Factors  : {factors[0]} and {factors[1]}")
    print("=" * 50)

if __name__ == "__main__":
    main()
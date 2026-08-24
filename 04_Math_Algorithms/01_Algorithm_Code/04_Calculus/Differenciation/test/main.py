"""
Main Execution & Testing Suite for the Math Engine.

This script serves as the playground to verify all mathematical operations,
calculus rules, and simplification logic built into the engine. It tests:
1. Basic Arithmetic & Polynomials
2. The Product and Quotient Rules
3. Complex Chain Rule combinations
4. Transcendental Functions (Log, Exp, Trigonometry)
"""
import sys
import os
current_dir = os.path.dirname(os.fspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from core.container import Expression
from core.primitives import Constant, Variable
from operations.arithmetic import Power
from operations.functions import log, exp, sin, cos, tan, cot, sec, cosec, e, pi

# Initialize the primary variable for derivation
x = Variable('x')

print("\n" + "="*50)
print("🚀 INITIALIZING ADVANCED CALCULUS TEST SUITE 🚀")
print("="*50)


print("\n--- TEST 1: Legacy Expression Container ---")
legacy_exp = Expression(Power(x, Constant(3)))
print(f"Original: {legacy_exp}")
print(f"Derived:  {legacy_exp.derive()}")


print("\n--- TEST 2: Standard Polynomials ---")
poly_eq = 5 * x**2 + 3 * x + 2
print(f"Original: {poly_eq}")
print(f"Derived:  {poly_eq.derive().simplify()}")

poly_diff = x**3 - x**2
print(f"Original: {poly_diff}")
print(f"Derived:  {poly_diff.derive().simplify()}")


print("\n--- TEST 3: Complex Numbers & Constants ---")
# (-4)**0.5 evaluates to a complex number. The engine should handle it safely.
complex_eq = x**3 / (-4)**0.5
print(f"Original: {complex_eq}")
print(f"Derived:  {complex_eq.derive().simplify()}")


print("\n--- TEST 4: The Product Rule & Transcendentals ---")
# Testing d/dx [x * ln(x) + e^x * e]
trans_eq = (x) * log(x) + exp(x) * e
print(f"Original: {trans_eq}")
print(f"Derived:  {trans_eq.derive().simplify()}")


print("\n--- TEST 5: Trigonometry (Product vs Power Rule) ---")
# Testing Product Rule on Trigonometry
trig_prod = sin(x) * sin(x)
print(f"Original: {trig_prod}")
print(f"Derived:  {trig_prod.derive().simplify()}")

# Testing Power & Chain Rule on Trigonometry (The bug we fixed earlier)
trig_power = sin(x)**2
print(f"Original: {trig_power}")
print(f"Derived:  {trig_power.derive().simplify()}")


print("\n--- TEST 6: The Quotient Rule (Advanced) ---")
# Testing d/dx [tan(x) / log(x)]
quotient_eq = tan(x) / log(x)
print(f"Original: {quotient_eq}")
print(f"Derived:  {quotient_eq.derive().simplify()}")


print("\n--- TEST 7: Deep Chain Rule (Boss Level) ---")
# Testing d/dx [sec(x^3)] -> Should yield sec(x^3)*tan(x^3) * 3x^2
chain_eq = sec(x**3)
print(f"Original: {chain_eq}")
print(f"Derived:  {chain_eq.derive().simplify()}")


print("\n--- TEST 8: Nested Exponential & Trigonometry ---")
# Testing d/dx [e^(cos(x))] -> Should yield e^(cos(x)) * -sin(x)
nested_eq = exp(cos(x))
print(f"Original: {nested_eq}")
print(f"Derived:  {nested_eq.derive().simplify()}")

print("\n" + "="*50)
print("✅ ALL TESTS EXECUTED SUCCESSFULLY ✅")
print("="*50 + "\n")
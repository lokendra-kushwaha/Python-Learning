"""
====================================================================================
📐 STANDARD LIBRARY: THE 'math' MODULE
====================================================================================
Description: The 'math' module provides access to the mathematical functions 
             defined by the C standard. It is highly optimized and much faster 
             than writing your own math logic in pure Python.
====================================================================================
"""

import math

def section_divider(title):
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")

# 🟢 1. MATHEMATICAL CONSTANTS
# ====================================================================================
section_divider("1. CONSTANTS (Built-in Values)")

print(f"-> Pi (π)   : {math.pi}")       # Ratio of a circle's circumference to its diameter
print(f"-> Euler (e): {math.e}")        # Base of the natural logarithm
print(f"-> Infinity : {math.inf}")      # Positive infinity (useful for comparisons)
print(f"-> NaN      : {math.nan}")      # Not a Number (used in data science for missing data)


# 🟢 2. ROUNDING AND TRUNCATION
# ====================================================================================
section_divider("2. ROUNDING NUMBERS")
num = 4.72

print(f"Original Number: {num}")
print(f"-> math.ceil()  : {math.ceil(num)} (Rounds UP to the nearest integer)")
print(f"-> math.floor() : {math.floor(num)} (Rounds DOWN to the nearest integer)")
print(f"-> math.trunc() : {math.trunc(num)} (Simply chops off the decimal part)")


# 🟢 3. POWER AND ROOTS
# ====================================================================================
section_divider("3. POWERS & ROOTS")

print(f"-> math.pow(2, 3) : {math.pow(2, 3)} (2 raised to power 3, returns float)")
print(f"-> math.sqrt(25)  : {math.sqrt(25)} (Square root of 25)")
print(f"-> math.isqrt(26) : {math.isqrt(26)} (Integer square root - rounds down to 5)")


# 🟢 4. ADVANCED MATH (Combinatorics & Algorithms)
# ====================================================================================
section_divider("4. ADVANCED MATH (GCD, LCM & Factorial)")

# Factorial: 5! = 5 * 4 * 3 * 2 * 1
print(f"-> math.factorial(5) : {math.factorial(5)}")

# GCD (Greatest Common Divisor): Largest number that divides both
print(f"-> math.gcd(24, 36)  : {math.gcd(24, 36)}")

# LCM (Least Common Multiple): Smallest number divisible by both (Python 3.9+)
print(f"-> math.lcm(4, 6)    : {math.lcm(4, 6)}")


# 🟢 5. TRIGONOMETRY (Angles & Degrees)
# ====================================================================================
section_divider("5. TRIGONOMETRY")

angle_degrees = 90
# Math functions require radians, so we convert it first
angle_radians = math.radians(angle_degrees)

print(f"-> 90 Degrees in Radians : {angle_radians}")
print(f"-> math.sin(90°)         : {math.sin(angle_radians)}")
print(f"-> math.cos(90°)         : {math.cos(angle_radians):.1f} (Almost 0)")

print("\n" + "=" * 60)
print("🎯 CONCLUSION: The 'math' module handles heavy lifting natively in C.")
print("=" * 60)
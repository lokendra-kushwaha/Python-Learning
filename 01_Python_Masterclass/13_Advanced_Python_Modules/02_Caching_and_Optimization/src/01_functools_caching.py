"""
====================================================================================
🚀 ADVANCED PYTHON: CACHING WITH 'functools'
====================================================================================
Description: A comprehensive guide to Python's built-in caching mechanisms.
             Caching stores the results of expensive function calls and returns 
             the cached result when the same inputs occur again.

Core Tools Covered:
1. @lru_cache       : Least Recently Used Cache (Limited memory, evicts old data).
2. @cache           : Unlimited Cache (Stores everything, Python 3.9+).
3. @cached_property : Lazy evaluation for Object-Oriented Programming (OOP).
====================================================================================
"""

import time
from functools import lru_cache, cache, cached_property

def section_divider(title):
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")

# 🟢 1. THE LRU CACHE (@lru_cache)
# ====================================================================================
"""
CONCEPT: 
LRU stands for "Least Recently Used". It saves a limited number of results in memory. 
If the cache gets full (e.g., maxsize=3), it automatically deletes the oldest, 
least-used result to make room for new data. This prevents RAM crashes!
"""
section_divider("1. THE LRU CACHE (@lru_cache)")

@lru_cache(maxsize=3)
def fetch_user_profile(user_id):
    print(f"   [Server] Fetching data for User {user_id} from database... (Takes 2s)")
    time.sleep(2) # Simulating a slow database query
    return f"User_{user_id}_Data"

print("-> First call for User 101 (Cache Miss):")
start = time.perf_counter()
print("   Result:", fetch_user_profile(101))
print(f"   ⏱️ Time: {time.perf_counter() - start:.2f} seconds\n")

print("-> Second call for User 101 (Cache Hit):")
start = time.perf_counter()
# This will execute instantly without hitting the database!
print("   Result:", fetch_user_profile(101))
print(f"   ⏱️ Time: {time.perf_counter() - start:.5f} seconds")


# 🟢 2. THE UNLIMITED CACHE (@cache)
# ====================================================================================
"""
CONCEPT:
Introduced in Python 3.9, @cache is simply @lru_cache(maxsize=None). 
It stores EVERY result permanently in memory. 
Use Case: Perfect for heavy mathematical algorithms (like recursion/Fibonacci) 
where inputs are limited but calculations are massive.
"""
section_divider("2. THE UNLIMITED CACHE (@cache)")

@cache
def heavy_math_algorithm(number):
    print(f"   [CPU] Crunching massive numbers for {number}... (Takes 2s)")
    time.sleep(2)
    return number * number * number

print("-> Processing number 5 (First Time):")
heavy_math_algorithm(5)

print("-> Processing number 5 (Second Time):")
start = time.perf_counter()
print("   Result:", heavy_math_algorithm(5))
print(f"   ⏱️ Time: {time.perf_counter() - start:.5f} seconds (Instant!)")


# 🟢 3. THE OOP MAGIC (@cached_property)
# ====================================================================================
"""
CONCEPT:
Used inside Classes (OOP). It transforms a method into a "property" (attribute) 
that is calculated only ONCE. 
Real-World Example: An E-commerce Cart (Amazon). The total bill is calculated 
only when the user opens the cart for the first time. If they go back and open 
the cart again, it loads instantly from memory!
"""
section_divider("3. THE OOP MAGIC (@cached_property)")

class AmazonCart:
    def __init__(self, username):
        self.username = username
        self.items = [1200, 450, 3000, 150] # Prices of items in cart
        print(f"   🛒 Cart created for {self.username}. No calculations done yet (Lazy Loading).")

    @cached_property
    def total_bill(self):
        """Calculates total price + tax. Runs only once per object instance!"""
        print(f"   [Server] Calculating total bill for {self.username}... (Takes 2s)")
        time.sleep(2) # Simulating complex tax and discount calculations
        total = sum(self.items)
        tax = total * 0.18 # 18% GST
        return total + tax
    

# Execution
my_cart = AmazonCart("Lokendra")

print("\n-> User clicks on 'Cart' icon (First Access):")
start = time.perf_counter()
# NOTE: We access it as a variable (my_cart.total_bill), NOT as a function!
print(f"   Total Bill: ₹{my_cart.total_bill}")
print(f"   ⏱️ Load Time: {time.perf_counter() - start:.2f} seconds\n")

print("-> User goes back and clicks 'Cart' again (Second Access):")
start = time.perf_counter()
# Magic happens here! The server is bypassed completely.
print(f"   Total Bill: ₹{my_cart.total_bill}")
print(f"   ⏱️ Load Time: {time.perf_counter() - start:.5f} seconds (Zero loading!)")

print("\n" + "=" * 70)
print("🎯 CONCLUSION: Caching saves CPU time, Database load, and User patience!")
print("=" * 70)
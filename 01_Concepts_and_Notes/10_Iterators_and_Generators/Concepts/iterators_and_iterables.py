# 🌟 ================================================================================= 🌟
# 🚀                                ITERATORS & ITERABLES 
# 🌟 ================================================================================= 🌟

# 💡 1. WHAT IS AN ITERATION?
# Iteration is a general term for taking each item of something, one after another. 
# Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration.

# Example:
num = [1, 2, 3]
for i in num:
    print(i)


# ⚙️ ================================================================================= ⚙️
# 🧠 2. LISTS VS ITERATORS (THE MEMORY BATTLE)
# ⚙️ ================================================================================= ⚙️
# An Iterator is an object that allows the programmer to traverse through a sequence of data 
# WITHOUT having to store the entire data in the memory at once.

import sys

# Scenario A: Using a List (Eager Evaluation)
L = [x for x in range(1, 10000)]
print(f"Memory size of List (L): {sys.getsizeof(L)/1024} KB")

# Scenario B: Using a Range (Lazy Evaluation)
x = range(1, 10000)
print(f"Memory size of Range (x): {sys.getsizeof(x)/1024} KB")

# █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
# 🧠 EXPLANATION: WHAT IS HAPPENING AT THE MEMORY LEVEL?
# 
# 🔴 List [1 to 10k]: It physically creates 10,000 integer objects in the RAM at once. 
# If you increase it to 10 Crore, your RAM will hit 100% and your PC will crash (O(N) Space).
# 
# 🟢 Range (Iterator Pattern): It DOES NOT store the numbers. It only stores the 
# rules: start=1, end=10000, step=1. 
# When a loop runs, it generates ONE number, hands it to the CPU, and immediately 
# DESTROYS it from RAM to make space for the next one. 
# Therefore, its size is ALWAYS small (O(1) Space), even for 10 Crore numbers!
# █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█


# 📦 ================================================================================= 📦
# 🔍 3. THE HOLY TRINITY: ITERABLE, ITERATOR, AND ITERATION
# 📦 ================================================================================= 📦

L = [1, 2, 3]
print(type(L)) # <class 'list'> -> L is an Iterable

iter_L = iter(L)
print(type(iter_L)) # <class 'list_iterator'> -> iter_L is an Iterator

# █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
# 🧠 EXPLANATION: THE DEFINITIVE SUMMARY
# 
# 1. ITERABLE (The Container): An object that holds data and CAN be looped over. 
#    (Example: List, String, Range). It only has the `__iter__` method.
# 2. ITERATOR (The Engine): The hidden engine that actively fetches the next item. 
#    It has BOTH `__iter__` and `__next__` methods.
# 3. ITERATION (The Action): The physical process of moving from item 1 to item 2.
#
# 📌 Analogy:
# Iterable = A Water Tank (Holds water, but doesn't flow on its own).
# Iterator = The Water Pump (Actively pulls the water out drop by drop).
# Iteration = The flow of the water drops.
#
# 🏆 GOLDEN RULES: 
# - Every Iterator is also an Iterable.
# - NOT all Iterables are Iterators (e.g., A List is an Iterable, but not an Iterator).
# - Every Iterable has an `__iter__` function.
# - Every Iterator has BOTH an `__iter__` function AND a `__next__` function.
# █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█


# 🕵️ ================================================================================= 🕵️
# 🕵️ 4. THE `dir()` CHECK (HOW TO IDENTIFY THEM IN MEMORY)
# 🕵️ ================================================================================= 🕵️

# First method to know if an object is iterable or not.
# Output -> TypeError: 'int' object is not iterable -> Because we cannot run loops on integers, so it is not iterable.

a = 2
# for i in a:
#   print(i) # 🚨 TypeError: 'int' object is not iterable.


print("Is Int Iterable?:", '__iter__' in dir(a)) # False.

T = {1:2, 3:4}
print("Is Dict Iterable?:", '__iter__' in dir(T)) # True.

# --- The Difference between Iterable and Iterator ---
L = [1, 2, 3]
print("List dir:", '__iter__' in dir(L), '| __next__' in dir(L)) 
# Output: True | False -> (L is an Iterable, but NOT an Iterator)

iter_L = iter(L)
print("Iterator dir:", '__iter__' in dir(iter_L), '| __next__' in dir(iter_L)) 
# Output: True | True -> (Now it is an Iterator)

# █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
# 🧠 EXPLANATION: WHY DOES THE LIST LACK `__next__`?
# 
# Question: "Why did `next` appear in `iter_L` but not in `L`?"
# Logic: Separation of Concerns! 
# A List is just a database. It shouldn't track loop progress. 
# Imagine 5 different `for` loops reading the same List simultaneously. If the List 
# itself had the `__next__` cursor, all 5 loops would fight over the exact same index 
# and the code would crash!
# 
# That's why Python generates a BRAND NEW, independent Iterator object (`iter_L`) for 
# every loop. Each iterator tracks its own private `__next__` cursor.
# █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█


# 🔄 ================================================================================= 🔄
# 🛠️ 5. DECONSTRUCTING THE NATIVE `FOR` LOOP
# 🔄 ================================================================================= 🔄
# A `for` loop is just syntactic sugar. Here is what actually happens:

num = [1, 2, 3]

# Step 1: Python fetches the Iterator engine
iter_num = iter(num)

# Step 2: Python aggressively calls next()
print(next(iter_num)) # Prints 1
print(next(iter_num)) # Prints 2
print(next(iter_num)) # Prints 3
# print(next(iter_num)) # 🚨 Raises StopIteration Exception!

# █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
# 🧠 EXPLANATION: BUILDING OUR OWN SYSTEM-LEVEL LOOP
# Let's write the exact Python Backend logic for a loop:
# █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█

def my_for_loop(iterable):
    # 1. Ask the Iterable object to spawn its engine (Iterator)
    iterator = iter(iterable) 
    
    # 2. Trigger an infinite loop
    while True: 
        try:
            # 3. Pull the next data point into memory
            print(next(iterator)) 
        
        except StopIteration:
            # 4. EXCEPTION CAUGHT: The iterator is empty. Break the loop safely.
            break  

print("\n--- Testing Custom For Loop ---")
a = [1,2,3]
b = range(1,11)
c = (1,2,3)
d = {1,2,3}
e = {0:1,1:1}

my_for_loop(a) # Try passing b, c, d, e here!


# ❓ ================================================================================= ❓
# 🧩 6. THE CONFUSING POINT (ITERATOR OF AN ITERATOR)
# ❓ ================================================================================= ❓

num = [1, 2, 3]
iter_obj1 = iter(num)
print(id(iter_obj1), '-> Address of Iterator 1')

iter_obj2 = iter(iter_obj1)
print(id(iter_obj2), '-> Address of Iterator 2')

# █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
# 🧠 EXPLANATION: WHY ARE THE MEMORY IDs IDENTICAL?
# 
# Question: "When we run `iter` on an iterator, we get the same ID. Why?"
# Logic: 
# Remember the rule: "Every Iterator is ALSO an Iterable." 
# This means Python demands that an Iterator must have an `__iter__()` method.
# But... an Iterator is ALREADY an engine! It makes no sense for an engine to build 
# another engine. 
# So, the CPython code for an Iterator's `__iter__` method is literally just:
# `return self`
# It hands back its OWN memory address! That is why the IDs match perfectly.
# █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█


# 🏗️ ================================================================================= 🏗️
# 👨‍💻 7. BUILDING OUR OWN `range()` (OOP SYSTEM DESIGN)
# 🏗️ ================================================================================= 🏗️

# Part 1: The Iterable (The Container)
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        # Spawns a new engine whenever a loop starts
        return MyRangeIterator(self)
    
# Part 2: The Iterator (The Engine)
class MyRangeIterator:
    def __init__(self, iterable_obj):
        self.iterable = iterable_obj 
    
    def __iter__(self): 
        return self # Fulfilling the Rule: returning itself
    
    def __next__(self): 
        # The Core Logic
        if self.iterable.start >= self.iterable.end:
            raise StopIteration # Send the kill signal to the loop
            
        current = self.iterable.start
        self.iterable.start += 1 # Move the cursor
        return current
    
print("\n--- Testing OOP Custom Range ---")
for i in MyRange(1, 5):
    print(i)

x = MyRange(1, 5)
print("Type of x:", type(x))
print("Type of iter(x):", type(iter(x)))


# 🤖 ================================================================================= 🤖
# 🚀 8. REAL-WORLD DATA SCIENCE APPLICATIONS (WHY THIS MATTERS)
# 🤖 ================================================================================= 🤖
# █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
# 🧠 EXPLANATION: ITERATORS IN MACHINE LEARNING
# 
# Application: If you have a 500 GB dataset of images for Deep Learning, and your 
# laptop only has 16 GB of RAM, you cannot use a List. Your PC will crash.
# 
# Solution: You use an Iterator (Like PyTorch's `DataLoader`).
# 1. The Iterator goes to the Hard Drive.
# 2. It pulls ONLY a "batch" of 32 images into the RAM.
# 3. The ML model trains on those 32 images.
# 4. The Iterator DELETES those 32 images from the RAM and fetches the next 32.
# 
# Result: You just processed 500 GB of data using barely 1 GB of RAM!
# 
# Next Step ➡️ Generators (An incredibly efficient way to make Iterators in just 
# 3 lines of code using the `yield` keyword).
# █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
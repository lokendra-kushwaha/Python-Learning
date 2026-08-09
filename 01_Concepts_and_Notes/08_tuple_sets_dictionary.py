"""
=============================================================================
Day 8 (Part 1): Tuples in Python
=============================================================================
This module covers everything about Python Tuples: creation, accessing items, 
immutability rules, tuple operations/functions, unpacking, and a practical 
performance/memory benchmark against Lists.
"""

# ---------------------------------------------------------
# 1. TUPLE BASICS & CREATION
# ---------------------------------------------------------
# Tuples are IMMUTABLE (cannot be changed), whereas Lists are MUTABLE.

t1 = ()
print("Empty tuple:", t1) 

# Single item tuple (Comma is mandatory, otherwise Python treats it as an int/string)
t2 = (2,) 
t2_str = ('hello',)
print("Single item tuple:", t2_str)
print("Type of t2_str:", type(t2_str))

# Homogeneous tuple (All items have the same datatype)
t3 = (1, 2, 3, 4) 

# Heterogeneous tuple (Different datatypes)
t4 = (1, True, None, 2.5) 
print("Heterogeneous tuple:", t4)

# Nested tuple
t5 = (1, 2, 3, (4, 5))
print("Nested tuple:", t5)

# Using type conversion 
t6 = tuple('hello')
print("String to Tuple:", t6)


# ---------------------------------------------------------
# 2. ACCESSING ITEMS
# ---------------------------------------------------------
print("\n--- Accessing Items ---")

# Indexing
t3 = (1, 2, 3, 4)
print("Positive Indexing (t3[2]):", t3[2])
print("Negative Indexing (t3[-1]):", t3[-1])

t5 = (1, 2, 3, (4, 5))
print("Nested Indexing (t5[3][0]):", t5[3][0])

# Slicing
t3 = (1, 2, 3, 4)
print("Slicing [1:3]:", t3[1:3])
print("Negative Slicing [-3:-1]:", t3[-3:-1])


# ---------------------------------------------------------
# 3. EDITING, ADDING & DELETING (IMMUTABILITY)
# ---------------------------------------------------------
print("\n--- Editing & Deleting ---")

t3 = (1, 2, 3, 4)

# Editing Items
# t3[3] = 1 # Throws TypeError: 'tuple' object does not support item assignment

# Adding Items
# Not possible because changes are not allowed in tuples.

# Deleting Items
# del t3[2] # Cannot delete specific items from a tuple.

# However, you CAN delete the entire tuple object from memory
del t3
# print(t3) # This would throw a NameError because t3 is gone.


# ---------------------------------------------------------
# 4. OPERATIONS ON TUPLES
# ---------------------------------------------------------
print("\n--- Operations ---")

# Arithmetic Operators (+ and *)
t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)
print("Concatenation (+):", t1 + t2) 
print("Repetition (*):", t1 * 3)

# Membership Operators
print("Is 1 in t1?:", 1 in t1)
print("Is 1 not in t1?:", 1 not in t1)

# Iteration with a loop
print("Looping through tuple:")
for i in t1:
    print(i, end=" ")
print()


# ---------------------------------------------------------
# 5. TUPLE FUNCTIONS
# ---------------------------------------------------------
print("\n--- Tuple Functions ---")

t = (1, 2, 3, 4)
print("Length:", len(t))
print("Minimum:", min(t))
print("Maximum:", max(t))
print("Sum of items:", sum(t))
print("Sorted (Returns a LIST in ASC order):", sorted(t)) 
print("Sorted (DESC order):", sorted(t, reverse=True)) 

# Count and Index
t_dup = (1, 2, 3, 4, 1)
print("Count of 1:", t_dup.count(1))
print("Index of first 1:", t_dup.index(1))


# ---------------------------------------------------------
# 6. BENCHMARKING: LIST VS TUPLE (Performance & Memory)
# ---------------------------------------------------------
print("\n--- List vs Tuple: Speed & Memory Test ---")
import time 
import sys

# Speed Test
L = list(range(10000000)) # Reduced zeroes slightly for safe execution
T = tuple(range(10000000))

start = time.time()
for i in L:
    i * 5
print('List iteration time:', time.time() - start)

start = time.time()
for i in T:
    i * 5
print('Tuple iteration time:', time.time() - start)

# Memory Test
L_small = list(range(1000))
T_small = tuple(range(1000))

print('List size in memory (bytes):', sys.getsizeof(L_small))
print('Tuple size in memory (bytes):', sys.getsizeof(T_small))

# ---------------------------------------------------------
# 7. MUTABILITY VS IMMUTABILITY IN VARIABLES
# ---------------------------------------------------------
print("\n--- Aliasing and Reassignment ---")

# Lists (Mutable) - Appending changes the original object in memory
a = [1, 2, 3]
b = a
a.append(4)
print("List 'a' after append:", a)
print("List 'b' also changes:", b)

# Tuples (Immutable) - Concatenation creates a completely NEW object
a = (1, 2, 3, 4)
b = a
a = a + (4,) # Reassigning 'a' to a new memory location
print("Tuple 'a' after reassignment:", a)
print("Tuple 'b' remains unchanged:", b)


# ---------------------------------------------------------
# 8. TUPLE UNPACKING & ZIPPING
# ---------------------------------------------------------
print("\n--- Unpacking & Zipping ---")

# Tuple unpacking
a, b, c = (1, 2, 3)
print("Unpacked values:", a, b, c)

# a, b = (1, 2, 3) # Throws ValueError: too many values to unpack

# Swap values (Pythonic way using tuples implicitly)
a = 1
b = 2
a, b = b, a
print("Swapped values:", a, b)

# Advanced unpacking with * (Asterisk)
a, b, *others = (1, 2, 3, 4)
print("First two unpacked:", a, b)
print("Remaining packed into a list:", others)

# Zipping tuples
a = (1, 2, 3, 4)
b = (5, 6, 7, 8) # Corrected duplicate 5 to 6 to make logic clearer

print("Zipped as list of tuples:", list(zip(a, b)))
print("Zipped as tuple of tuples:", tuple(zip(a, b)))

"""
=============================================================================
Day 8 (Part 2): Sets in Python
=============================================================================
This module covers Sets in Python: creation, mutability constraints, 
adding/deleting items, mathematical set operations (Union, Intersection, etc.), 
Frozensets, and Set Comprehensions.
"""

# ---------------------------------------------------------
# 1. CREATING SETS
# ---------------------------------------------------------

s = {} # Creates an Empty Dictionary, not a set!
print("Empty curly braces:", s)
print("Type of {}:", type(s)) # This is not set.

# Right syntax for empty set
s = set()
print("Correct empty set:", s) # This is an empty set.

# 1D set
s1 = {1, 2, 3}
print("1D set:", s1)

# 2D set
# s2 = {2, 3, {1, 2}} 
# print(s2) # Throws TypeError! Mutable datatypes (like lists, sets, dicts) are not allowed inside a set.

# Heterogeneous set
s3 = {'hello', True, 1}
# True is treated as 1 in Python, and sets don't contain duplicates, so True and 1 merge.
print("Heterogeneous set:", s3) 

s4 = {'hello', True, 1, (1, 2)}
print("Order doesn't matter:", s4) 

# Type conversion
s4 = set([1, 2, 34])
print("List to Set:", s4)

# Duplicates not allowed
s = {1, 1, 2, 2, 3}
print("Set with duplicates removed:", s)

# Set can't have mutable items
# s = {1, 2, 3, [4, 5]}
# print(s) # Throws TypeError: unhashable type: 'list'

# Unordered nature
s1 = {1, 2, 3}
s2 = {3, 2, 1}
print("Is {1,2,3} == {3,2,1}?:", s1 == s2) # Output is True because order doesn't matter.


# ---------------------------------------------------------
# 2. ACCESSING & EDITING ITEMS
# ---------------------------------------------------------
print("\n--- Accessing & Editing ---")

s1 = {1, 2, 3}
# print(s1[0]) # Throws TypeError: 'set' object is not subscriptable (unordered)

# Editing items
# s1[0] = 100 # Throws TypeError. You cannot edit items by index.


# ---------------------------------------------------------
# 3. ADDING ITEMS
# ---------------------------------------------------------
print("\n--- Adding Items ---")
s1 = {1, 2, 3}

# add -> Adds a single item
s1.add(5)
print("After add(5):", s1)

# update -> Adds multiple items from an iterable
s1.update([5, 6, 7])
print("After update([5,6,7]):", s1)


# ---------------------------------------------------------
# 4. DELETING ITEMS
# ---------------------------------------------------------
print("\n--- Deleting Items ---")

# del
s = {1, 2, 3}
del s
# del s[0] # Throws TypeError
# print(s) # Throws NameError as 's' is deleted from memory.

# discard -> Deletes specific item, DOES NOT throw error if item doesn't exist
s1 = {1, 2, 3}
s1.discard(3) 
print("After discard(3):", s1)

# remove -> Deletes specific item, THROWS ERROR if item doesn't exist
s = {1, 2, 3}
s.remove(3)
# s.remove(5) # Throws KeyError because 5 doesn't exist in set
print("After remove(3):", s)

# pop -> Randomly deletes an item
s1 = {1, 2, 3}
s1.pop() 
print("After pop():", s1)

# clear -> Empties the set completely
s1 = {1, 2, 3}
s1.clear()
print("After clear():", s1) 


# ---------------------------------------------------------
# 5. MATHEMATICAL OPERATIONS ON SETS
# ---------------------------------------------------------
print("\n--- Set Operations ---")

s1 = {1, 2, 3}
s2 = {5, 2, 7}

# Union (|)
print("Union (s1 | s2):", s1 | s2)

# Intersection (&)
print("Intersection (s1 & s2):", s1 & s2)

# Difference (-)
print("Difference (s1 - s2):", s1 - s2)
print("Difference (s2 - s1):", s2 - s1)

# Symmetric difference (^)
print("Symmetric Difference (s1 ^ s2):", s1 ^ s2)

# Membership test
print("Is 1 in s1?:", 1 in s1)
print("Is 1 not in s1?:", 1 not in s1)

# Loops
print("Iterating over set:")
for i in s1:
    print(i, end=" ")
print()


# ---------------------------------------------------------
# 6. SET FUNCTIONS & METHODS
# ---------------------------------------------------------
print("\n--- Set Functions ---")

# len / min / max / sum / sorted
s = {1, 2, 3}
print("Length:", len(s))
print("Sum:", sum(s))
print("Min:", min(s))
print("Max:", max(s))
print("Sorted (ASC, returns List):", sorted(s))
print("Sorted (DESC):", sorted(s, reverse=True)) 

# Union / Update methods
s1 = {1, 2, 3}
s2 = {5, 2, 6}
print("\nunion():", s1.union(s2))
s1.update(s2) 
print("After update, s1:", s1)
print("After update, s2:", s2)

# Intersection / Update methods
s1 = {1, 2, 3}
s2 = {5, 2, 6}
print("\nintersection():", s1.intersection(s2))
s1.intersection_update(s2) 
print("After intersection_update, s1:", s1)
print("After intersection_update, s2:", s2)

# Difference / Update methods
s1 = {1, 2, 3}
s2 = {5, 2, 6}
print("\ndifference():", s1.difference(s2))
s1.difference_update(s2)
print("After difference_update, s1:", s1)
print("After difference_update, s2:", s2)

# Symmetric Difference / Update methods
s1 = {1, 2, 3}
s2 = {5, 2, 6}
print("\nsymmetric_difference():", s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print("After symmetric_difference_update, s1:", s1)
print("After symmetric_difference_update, s2:", s2)

# isdisjoint / issubset / issuperset
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print("\nisdisjoint?:", s1.isdisjoint(s2)) # Output is False because some items are common

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5}
print("issubset?:", s2.issubset(s1)) # Output is True because all s2 items are present in s1
print("issuperset?:", s1.issuperset(s2))

# Copy
s1 = {1, 2, 3}
s2 = s1.copy()
print("\nOriginal:", s1)
print("Copied:", s2)


# ---------------------------------------------------------
# 7. FROZENSET
# ---------------------------------------------------------
# Frozen set is just an immutable version of a Python's set object.
print("\n--- Frozenset ---")
fs1 = frozenset([1, 2, 3])
print("Frozenset 1:", fs1)
fs2 = frozenset([3, 4, 5])
print("Union of Frozensets:", fs1.union(fs2))

# 2D frozen set
fs = frozenset([1, 2, frozenset([4, 5])]) 
print("2D Frozenset:", fs)

# All standard set functions will work on frozenset also (except ones that mutate it).


# ---------------------------------------------------------
# 8. SET COMPREHENSION
# ---------------------------------------------------------
print("\n--- Set Comprehension ---")

s = {i for i in range(1, 11)}
print("1 to 10:", s)

s = {i for i in range(1, 11) if i > 5}
print("Greater than 5:", s)

s = {i*i for i in range(1, 11)}
print("Squares:", s)

"""
=============================================================================
Day 8 (Part 3): Dictionaries in Python
=============================================================================
This module covers Dictionaries: creation (1D, 2D), accessing, adding, 
editing, deleting key-value pairs, dictionary functions, and advanced 
Dictionary Comprehensions (including nested and zipped).
"""

# ---------------------------------------------------------
# 1. CREATING DICTIONARIES
# ---------------------------------------------------------
print("--- Creating Dictionaries ---")

d = {} # Empty dict
print("Empty dict:", d)

# 1D Dict (Homogeneous keys/values)
d = {'name': 'lokendra', 'gender': 'male'} 
print("1D Dict:", d)

# Heterogeneous dictionary (Different datatypes for keys and values)
d = {(1, 2, 3): 1, 'hello': 'world'} 
print("Heterogeneous Dict:", d)

# 2D dictionary (Nested dictionary)
s = {
    'name': 'lokendra', 
    'college': 'bit', 
    'semester': '4th', 
    'subjects': {
        'dsa': 50,
        'maths': 67,
        'english': 34
    }
} 
print("2D (Nested) Dict:", s)

# Creating dict using dict() function with a list of tuples
d = dict([(1, 1), (2, 2), (3, 3), ('name', 'lokendra')])
print("Using dict() constructor:", d)

# Keys cannot be duplicated (The last assigned value overwrites the previous one)
d1 = {'name': 'lokendra', 'name': 'kushwaha'}
print("Duplicate keys handled:", d1) 

# Keys CANNOT be a mutable datatype (like lists, sets, or dicts)
# d = {'name': 'lokendra', [1, 2, 3]: 2}
# print(d) # Throws TypeError: unhashable type: 'list'

# Keys CAN be immutable datatypes (like tuples)
d = {'name': 'lokendra', (1, 2, 3): 2}
print("Tuple as a key:", d)


# ---------------------------------------------------------
# 2. ACCESSING ITEMS
# ---------------------------------------------------------
print("\n--- Accessing Items ---")
my_dict = {'name': 'lokendra', 'gender': 'male', 'age': 30}

# print(my_dict[0]) # Throws KeyError. Dictionaries are unordered, indexed by KEYS, not numbers.

my_dict = {'name': 'lokendra', 'gender': 'male', 'age': 20}
print("Access by key ['name']:", my_dict['name'])
print("Access by key ['age']:", my_dict['age'])

# get() method (Better practice: doesn't throw error if key is missing)
print("Using get('name'):", my_dict.get('name'))
print("Using get('age'):", my_dict.get('age'))

# Accessing nested dictionary items
print("Nested Access (Maths marks):", s['subjects']['maths'])


# ---------------------------------------------------------
# 3. ADDING & EDITING NEW KEY-VALUE PAIRS
# ---------------------------------------------------------
print("\n--- Adding & Editing Items ---")
d = {'name': 'lokendra', 'age': 20, 3: 3}

# Adding
d['gender'] = 'male'
d['weight'] = '60'
print("After adding gender and weight:", d)

# Adding to a nested dictionary
s['subjects']['ds'] = 89
print("After adding 'ds' to nested dict:", s['subjects'])

# Editing existing key-value pair
s['semester'] = '5th'  # Changed from '4th' to '5th' (Modified key name from user's 'sem' for consistency)
s['subjects']['dsa'] = 60
print("After editing semester and dsa marks:", s)


# ---------------------------------------------------------
# 4. REMOVING KEY-VALUE PAIRS
# ---------------------------------------------------------
print("\n--- Removing Items ---")

# pop() -> Removes specific key and returns its value
d = {'name': 'lokendra', 'age': 20, 3: 3}
d.pop(3)
print("After pop(3):", d)

# popitem() -> Removes the last inserted key-value pair
d = {'name': 'lokendra', 'age': 20, 3: 3}
d.popitem() 
print("After popitem():", d)

# del -> Deletes a key-value pair directly from memory
d = {'name': 'lokendra', 'age': 20, 3: 3}
del d['name']
print("After del d['name']:", d)

# Deleting from nested dictionary
del s['subjects']['maths']
print("After deleting 'maths' from nested dict:", s['subjects'])

# clear() -> Empties the entire dictionary
d = {'name': 'lokendra', 'age': 20, 3: 3}
d.clear()
print("After clear():", d) # Empty dict

# ---------------------------------------------------------
# 5. DICTIONARY OPERATIONS
# ---------------------------------------------------------
print("\n--- Dictionary Operations ---")

# Membership Operator (Checks ONLY in keys, not values)
print("Is 'name' a key in s?:", 'name' in s)
print("Is 'lokendra' a key in s?:", 'lokendra' not in s)

# Loops
d = {'name': 'lokendra', 'gender': 'male', 'age': 20}
print("\nLooping through keys:")
for i in d:
    print(i)

print("\nLooping through keys and values:")
for i in d:
    print(i, "->", d[i])


# ---------------------------------------------------------
# 6. DICTIONARY FUNCTIONS
# ---------------------------------------------------------
print("\n--- Dictionary Functions ---")
d = {'name': 'lokendra', 'gender': 'male', 'age': 20}

# len / sorted
print("Length:", len(d))
print("Sorted keys (ASC):", sorted(d)) # Output is a list of keys
print("Sorted keys (DESC):", sorted(d, reverse=True))

# items / keys / values
print("\nItems (Key-Value tuples):", d.items())
print("Keys:", d.keys())
print("Values:", d.values())

# update() -> Merges two dictionaries
d1 = {1: 2, 3: 4, 4: 5}
d2 = {4: 7, 6: 8} # Key '4' will be updated to 7
d1.update(d2)
print("\nAfter update():", d1)


# ---------------------------------------------------------
# 7. DICTIONARY COMPREHENSION
# ---------------------------------------------------------
print("\n--- Dictionary Comprehension ---")

# Simple comprehension
d_comp = {i: i**2 for i in range(1, 11)}
print("Squares dict:", d_comp)

# Using items() in comprehension
distances = {'delhi': 1000, 'mumbai': 2000, 'banglore': 3000}
miles_dict = {key: value * 0.62 for (key, value) in distances.items()}
print("Distances converted to miles:", miles_dict)

# Comprehension with zip()
day = ['sunday', 'monday', 'tuesday', 'wed', 'thurs', 'fri', 'sat']
temp_C = [30, 31, 23, 43, 54, 65, 56]
my_dict2 = {i: j for (i, j) in zip(day, temp_C)}
print("Zipped dictionary:", my_dict2)

# Comprehension with if condition
product = {'phone': 10, 'laptop': 0, 'charger': 32, 'tablet': 0}
available_products = {key: value for (key, value) in product.items() if value > 0}
print("Filtered products (value > 0):", available_products)

# Nested Comprehension (Creating multiplication tables)
# Output structure: {2: {1: 2, 2: 4...}, 3: {1: 3, 2: 6...}}
nested_dict = {i: {j: i * j for j in range(1, 11)} for i in range(2, 5)}
print("\nNested comprehension (Multiplication Tables):")
for key, value in nested_dict.items():
    print(f"Table of {key}: {value}")
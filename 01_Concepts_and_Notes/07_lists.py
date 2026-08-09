"""
=============================================================================
Day 7: Lists in Python
=============================================================================
This module covers everything about Python Lists: creation (1D, 2D, 3D), 
memory allocation concepts (id), indexing, slicing, mutation (adding/editing),
deletion, and list operations.
"""

# ---------------------------------------------------------
# 1. LIST BASICS & MEMORY ALLOCATION
# ---------------------------------------------------------
# Python Lists are Heterogeneous (different datatypes can be stored).

a = 2
print("ID of integer 'a':", id(a))

l = [1, 2, 3]
print("\nID of list 'l':", id(l))
print("ID of l[0] (which is 1):", id(l[0]))
print("ID of l[1] (which is 2):", id(l[1]))
print("ID of l[2] (which is 3):", id(l[2]))

print("\nID of integer 1:", id(1))
print("ID of integer 2:", id(2))
print("ID of integer 3:", id(3))

# Checking if order matters in lists
l = [1, 2, 3]
l1 = [1, 3, 2]
print("\nIs [1, 2, 3] equal to [1, 3, 2]?:", l == l1) # Order matters, so False


# ---------------------------------------------------------
# 2. CREATING A LIST
# ---------------------------------------------------------
print("\n--- Creating Lists ---")
print("Empty list:", []) 

# 1D List (Homogeneous: all items have same datatype)
print("1D List:", [1, 2, 3, 4]) 

# 2D list (Heterogeneous & nested: 4th item has list datatype)
print("2D List:", [1, 2, 3, 4, [4, 5]]) 

# 3D list (Homogeneous because all main items are lists)
print("3D List:", [[[1, 2], [3, 4]], [[1, 2], [3, 4]]]) 

# Heterogeneous list
print("Heterogeneous List:", [1, True, 'hello', 5.6, 5+6j])

# Using type conversion
print("String to List conversion:", list('hello'))


# ---------------------------------------------------------
# 3. ACCESSING ITEMS FROM A LIST
# ---------------------------------------------------------
print("\n--- Accessing Items ---")

# 1. Indexing
l = [1, 2, 3, 4]
print("Positive Indexing (First):", l[0]) 
print("Positive Indexing (Last):", l[3])
print("Negative Indexing (Last):", l[-1]) 
print("Negative Indexing (3rd from last):", l[-3])

# Indexing in 2D List
l = [1, 2, 3, [4, 5]]
print("2D List negative indexing:", l[-1][-2])

# Indexing in 3D List
l = [[[1, 2], [3, 4]], [[5, 2], [3, 4]]]
print("3D List nested indexing:", l[1][0][0])

# 2. Slicing
l = [1, 2, 3, 4]
print("\nSlicing [0:3]:", l[0:3])
print("Slicing (Reverse):", l[::-1])


# ---------------------------------------------------------
# 4. ADDING ITEMS TO A LIST
# ---------------------------------------------------------
print("\n--- Adding Items ---")

# 1. Append() --> Adds exactly one item at the end of the list
l = [1, 2, 3, 4, 5]
l.append(6)
l.append('lokendra')
print("After Append:", l)

# 2. Extend() --> Unpacks an iterable and adds multiple items
l = [1, 2, 3, 4, 5]
l.extend([6, 7, 8])
print("After Extend (with list):", l)

l = [1, 2, 3, 4, 5]
l.append([6, 7, 8]) # Notice the difference between append and extend here
print("After Append (with list):", l)

l = [1, 2, 3, 4, 5]
l.extend("delhi") # Unpacks the string into characters
print("After Extend (with string):", l)

# 3. Insert() --> Adds item at a specific location
l = [1, 2, 3, 4, 5]
l.insert(1, 100)
print("After Insert (at index 1):", l)


# ---------------------------------------------------------
# 5. EDITING ITEMS IN A LIST
# ---------------------------------------------------------
print("\n--- Editing Items ---")
l = [1, 2, 3, 4, 5]

# Editing with indexing
l[-1] = 500
print("Edited using Indexing:", l)

# Editing with slicing
l[1:4] = [200, 300, 400]
print("Edited using Slicing:", l)


# ---------------------------------------------------------
# 6. DELETING ITEMS FROM A LIST
# ---------------------------------------------------------
print("\n--- Deleting Items ---")

l = [1, 2, 3, 4, 5]
print("Original list before full deletion:", l)
del l
# print(l) # This would throw a NameError because 'l' is completely deleted from memory

l = [1, 2, 3, 4, 5]
# Indexing
del l[-1]
print("After del with index [-1]:", l)

# Slicing
del l[1:3]
print("After del with slicing [1:3]:", l)

# Remove() --> Takes the actual item value as an argument, not the index
l = [1, 2, 3, 4, 5]
l.remove(5)
print("After remove(5):", l)

# Pop() --> Removes item at a specific index and returns it (Default index is -1)
l = [1, 2, 3, 4, 5]
l.pop(0)
print("After pop(0):", l)
l.pop() 
print("After pop() (default last):", l) 

# Clear() --> Makes a list completely empty but keeps the list object in memory
l = [1, 2, 3, 4, 5]
l.clear() 
print("After clear():", l)

# ---------------------------------------------------------
# 7. OPERATIONS ON LISTS
# ---------------------------------------------------------
print("\n--- Operations ---")

# 1. Arithmetic Operators
l = [1, 2, 3, 4, 5]
l2 = [5, 6, 7]
print("Concatenation/Merging (+):", l + l2) 

l = [1, 2, 3, 4, 5]
print("Repetition (*):", l * 3) 

# 2. Membership Operators
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, [5, 6]]

print("\nIs 5 in l1?", 5 in l1) # Output is True
print("Is 5 not in l1?", 5 not in l1)
print("Is 5 in l2?", 5 in l2) # Output is False (5 is inside a nested list, not directly in l2)
print("Is [5, 6] in l2?", [5, 6] in l2) # Output is True

"""
=============================================================================
Day 7 (Part 2): Advanced Lists in Python
=============================================================================
This module covers list iteration, built-in list functions, list comprehensions 
(filtering and nesting), traversal techniques, the zip() function, and 
the critical difference between aliasing and copying (memory management).
"""

# ---------------------------------------------------------
# 8. LOOPS ON LISTS
# ---------------------------------------------------------
print("\n--- Loops on Lists ---")
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, [5, 6]]

print("Iterating l1:")
for i in l1:
    print(i)

print("Iterating l2 (Nested list handled as single item):")
for i in l2:
    print(i)


# ---------------------------------------------------------
# 9. LIST FUNCTIONS
# ---------------------------------------------------------
print("\n--- List Functions ---")

# len / min / max / sorted
l = [1, 2, 9, 3, 4, 5]
print("Length of list:", len(l))
print("Minimum value:", min(l)) # Works only when data is homogeneous
print("Maximum value:", max(l)) # Works only when data is homogeneous

print("Sorted (Default ASC Order, returns new list):", sorted(l)) 
print("Sorted (DESC Order):", sorted(l, reverse=True)) 

# Count --> Tells item's frequency count
l = [1, 3, 6, 8, 2, 4]
print("Count of 2:", l.count(2))

# Index --> Tells given item's index position
l = [1, 2, 9, 3, 4, 5]
print("Index of 2:", l.index(2))

# Reverse --> Permanently reverses the original list in-place
l = [1, 2, 9, 3, 4, 5]
l.reverse() 
print("List after reverse():", l)

# Sort --> Sorts the original list in-place (permanently)
l = [1, 2, 9, 3, 4, 5]
print("Original list:", l)
print("Using sorted() [Temporary]:", sorted(l)) 
print("After sorted(), original is unchanged:", l)
l.sort() 
print("After sort() [Permanent]:", l)

# Copy --> Creates a Shallow Copy (New memory location, but nested items share refs)
l = [1, 2, 9, 3, 4, 5]
print("Original list:", l)
print("ID of original:", id(l))
l1 = l.copy()
print("Copied list:", l1)
print("ID of copied list:", id(l1))


# ---------------------------------------------------------
# 10. LIST COMPREHENSION
# ---------------------------------------------------------
# List comprehension provides a concise way of creating lists.
print("\n--- List Comprehension ---")

# Normal way vs Comprehension
l = []
for i in range(1, 11): 
    l.append(i)
print("Normal append:", l)

numlist = [i for i in range(1, 11)] 
print("Using Comprehension:", numlist)

# Scalar Multiplication Example
v = [2, 3, 4]
s = -3
x = [i * s for i in v]
print("Scalar multiplication (Comprehension):", x)

x = [] # Without comprehension
for i in v:
    x.append(i * s)
print("Scalar multiplication (Normal loop):", x)

# Generating squares
square = [i * i for i in range(100)]
# print(square) # (Skipped printing 100 items to keep console clean)

l = [1, 2, 3, 4]
squarelist = [i * i for i in l]
print("Squares of list items:", squarelist)

# Comprehension with If condition
l = [i for i in range(1, 51) if i % 5 == 0]
print("Multiples of 5:", l)

languages = ['java', 'python', 'php', 'c', 'javascript']
plang = [language for language in languages if language.startswith('p') == True]
print("Languages starting with 'p':", plang)

# Comprehension with multiple conditions
basket = ['apple', 'guava', 'cherry', 'banana']
my_fruits = ['apple', 'kiwi', 'grapes', 'banana']
l = [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]
print("Common fruits starting with 'a':", l)

# Nested Comprehensions (Matrices & Cartesian Products)
matrices = [[i * j for i in range(1, 4)] for j in range(1, 4)]
print("Matrix using nested comprehension:", matrices)

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l = [i * j for i in l1 for j in l2]
print("Cartesian product multiplication:", l)


# ---------------------------------------------------------
# 11. TRAVERSING A LIST (2 WAYS)
# ---------------------------------------------------------
print("\n--- Traversing a List ---")

# 1. Itemwise
print("Itemwise Traversal:")
l = [1, 2, 3, 4]
for i in l: 
    print(i)

# 2. Indexwise
print("Indexwise Traversal:")
l = [1, 2, 3, 4]
for i in range(0, len(l)): 
    print(f"Index {i} -> Item {l[i]}") 


# ---------------------------------------------------------
# 12. ZIP FUNCTION
# ---------------------------------------------------------
print("\n--- Zip Function ---")
l1 = [1, 2, 3, 4]
l2 = [-1, -2, -3, -4]

print("Zipped list of tuples:", list(zip(l1, l2)))

# Using zip inside list comprehension
x = [i + j for i, j in zip(l1, l2)]
print("Addition using zip:", x)


# ---------------------------------------------------------
# 13. ADVANCED CONCEPTS & MEMORY MANAGEMENT
# ---------------------------------------------------------
print("\n--- Advanced Concepts ---")

# Storing functions inside a list (First-class citizens)
l = [1, 2, print, type, input]
print("List containing functions:", l)

# Aliasing vs Copying (Mutability concept)
print("\n--- Aliasing (Assignment) ---")
a = [1, 2, 3]
b = a # Both 'a' and 'b' point to the exact same memory location
print("List a:", a)
print("List b:", b)

a.append(4)
print("After appending to 'a':")
print("List a:", a)
print("List b:", b) # 'b' is also changed because lists are mutable and share the same reference.

print("\n--- Copying (Shallow Copy) ---")
a = [1, 2, 3]
b = a.copy() # 'b' gets a completely new memory location

print("List a:", a)
print("List b:", b)

a.append(4)
print("After appending to 'a':")
print("List a:", a)
print("List b:", b) # 'b' is NOT changed because it has its own copy in memory.
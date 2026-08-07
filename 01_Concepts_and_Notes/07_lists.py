#==================================================================================================
#                              Day - 7 : Lists in Python
#==================================================================================================

# <--- Lists in Python --->

# Python List --> Hetrogenius (different datatype can be stored)

a = 2
print(id(a))

l = [1, 2, 3]

print(id(l))
print(id(l[0]))
print(id(l[1]))
print(id(l[2]))

print(id(1))
print(id(2))
print(id(3))

l = [1, 2, 3]
l1 = [1, 3, 2]
print(l == l1) # Order matters

# Creating a List -->

print([]) # A empty list

# 1D List
print([1, 2, 3, 4]) # 1D list (also a homogenius list because all items has same datatype)

# 2D list
print([1, 2, 3, 4, [4, 5]]) # This is a Hetrogenius list and a nested list also (4th items has list datatype)

# 3D list
print([[[1, 2], [3, 4]], [[1, 2], [3, 4]]]) # Homogenius list because list's item has only 1 datatype that is list

# Hetrogenius list
print([1, True, 'hello', 5.6, 5+6j])

# # Using type conversion
print(list('hello'))

# Accessing items from a list -->

# 1. Indexing -->
l = [1, 2, 3, 4]
print(l[0]) # Positive indexing
print(l[3])
print(l[-1]) # Negative indexing
print(l[-3])

l = [1, 2, 3, [4, 5]]
print(l[-1][-2])

l = [[[1, 2], [3, 4]], [[5, 2], [3, 4]]]
print(l[1][0][0])

# 2. Slicing
l = [1, 2, 3, 4]
print(l[0:3])
print(l[::-1])

# Adding Items to a list -->

# 1. Append() --> adding for one item in list
l = [1, 2, 3, 4, 5]
l.append(6)
l.append('lokendra')
print(l)

# 2. Extend --> Adding for multiple items
l = [1, 2, 3, 4, 5]
l.extend([6, 7, 8])
print(l)

l = [1, 2, 3, 4, 5]
l.append([6, 7, 8])
print(l)

l = [1, 2, 3, 4, 5]
l.extend("delhi")
print(l)

# Insert --> Add items in specific location
l = [1, 2, 3, 4, 5]
l.insert(1, 100)
print(l)

# Editing items in a list -->

l = [1, 2, 3, 4, 5]
# # Editing with indexing
l[-1] = 500
print(l)

# # Editing with slicing
l[1:4] = [200, 300, 400]
print(l)

# Deleting items from a list -->
l = [1, 2, 3, 4, 5]
print(l)
del l
# print(l)

l = [1, 2, 3, 4, 5]
# Indexing
del l[-1]
print(l)
# Slicing
del l[1: 3]
print(l)

# Remove --> Take item of list as an argument not index position
l = [1, 2, 3, 4, 5]
l.remove(5)
print(l)

# pop 
l = [1, 2, 3, 4, 5]
l.pop(0)
print(l)
l.pop() # Default index is -1
print(l) 

# clear
l = [1, 2, 3, 4, 5]
l.clear() # Make a list empty
print(l)

# Operations on lists -->
# 1. Arithmethic
# 2. Membership
# 3. loops

# Arithmetic Operators
l = [1, 2, 3, 4, 5]
l2 = [5, 6, 7]
print(l + l2) # Concatination/Merging
l = [1, 2, 3, 4, 5]
print(l*3) # Tree times merge

# Membership Operators
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, [5, 6]]

print(5 in l1) # Output is True
print(5 not in l1)
print(5 in l2) # Output is false
print([5, 6] in l2) # Output is true

# Loops
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, [5, 6]]

for i in l1:
    print(i)

for i in l2:
    print(i)

# <-- List Functions -->

# len/min/max/sorted -->
l = [1, 2, 9, 3, 4, 5]
print(len(l))
print(min(l)) # Works only when data is homogenius
print(max(l)) # Works only when data is homogenius
print(sorted(l)) # Default ASC Order
print(sorted(l, reverse=True)) # DESC order

# Count --> Tells item's frequency count
l = [1, 3, 6, 8, 2, 4]
print(l.count(2))

# Index --> Tell given item's index position
l = [1, 2, 9, 3, 4, 5]
print(l.index(2))

# Reverse -->
l = [1, 2, 9, 3, 4, 5]
l.reverse() # Permanently reverses the list
print(l)

# sort --> Just like sorting
l = [1, 2, 9, 3, 4, 5]
print(l)
print(sorted(l)) # Temporary operation not permanently
print(l)
l.sort() # Permanently sort
print(l)

# copy -> Creates Shallow copy not deep copy
l = [1, 2, 9, 3, 4, 5]
print(l)
print(id(l))
l1 = l.copy()
print(l1)
print(id(l1))

# <-- List Comprehension -->
# List comprehension provides a concise way of creating lists.

l = []
for i in range(1, 11): # normal way
    l.append(i)
print(l)

numlist = [i for i in range(1, 11)] # comprehension
print(numlist)

v = [2, 3, 4]
s = -3
x = [i*s for i in v]
print(x)

x = [] # Without comprehension
for i in v:
    x.append(i*s)
print(x)

square = [i*i for i in range(100)]
print(square)

l = [1, 2, 3, 4]

squarelist = [i*i for i in l]
print(squarelist)

l = [i for i in range(1, 51) if i%5 == 0]
print(l)

languages = ['java', 'python', 'php', 'c', 'javascript']

plang = [language for language in languages if language.startswith('p') == True]
print(plang)

basket = ['apple', 'guava', 'cherry', 'banana']
my_fruits = ['apple', 'kiwi', 'grapes', 'banana']

l = [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]
print(l)

matrices = [[i*j for i in range(1, 4)] for j in range(1, 4)]
print(matrices)

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

l = [i*j for i in l1 for j in l2]
print(l)

# 2 ways to traverse a list -->

# 1. Itemwise
l = [1, 2, 3, 4]
for i in l: # itemwise loop
    print(i)

# 2. Indexwise
l = [1, 2, 3, 4]
for i in range(0, len(l)): # Index wise loop
    print(i) # Prints index position
    print(l[i]) # Prints items

# Zip function -->
l1 = [1, 2, 3, 4]
l2 = [-1, -2, -3, -4]
#___________________________________
print(list(zip(l1, l2)))

x = [i+j for i, j in zip(l1, l2)]
print(x)
#___________________________________

l = [1, 2, print, type, input]
print(l)

a = [1, 2, 3]
b = a

print(a)
print(b)

a.append(4)
print(a)
print(b) # Changed because list are mmutable.

a = [1, 2, 3]
b = a.copy()

print(a)
print(b)

a.append(4)
print(a)
print(b) # Not changed because b has copy of a not a.
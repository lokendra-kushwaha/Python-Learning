#==================================================================================================
#                        Day - 8 : Tuple, Sets and Dictionary in Python
#==================================================================================================

# <--- Tuples --->
# Tupes are immutable and list are immutable

# Creating tuples -->

t1 = ()
print(t1) # Empty tuple

t2 = (2,) # Single item tuple
t2 = ('hello',)
print(t2)
print(type(t2))

t3 = (1, 2, 3, 4) # Homogenius tuple because it's items have only one datatype.

t4 = (1, True, None, 2.5) # Hetrogenius tuple
print(t4)

t5 = (1, 2, 3, (4, 5))
print(t5)

# Using type conversion 
t6 = tuple('hello')
print(t6)

# Accessing items -->

# Indexing
t3 = (1, 2, 3, 4)
print(t3[2])
print(t3[-1])
t5 = (1, 2, 3, (4, 5))
print(t5[3][0])

# # Slicing
t3 = (1, 2, 3, 4)
print(t3[1:3])
print(t3[-3:-1])

# Editing Items -->

t3 = (1, 2, 3, 4)
t3[3] = 1
# print(t3) # Throw an error because tuples are immutable.

# Adding items
t3 = (1, 2, 3, 4)
# Not possible because changes are not allowed in tuples.

# Deleting items -->
t3 = (1, 2, 3, 4)
# del t3[2] # Can not be deleted specific items.
print(t3)

del t3
print(t3) # This would work

# Operations on tuples -->

# Arithmetic Operator - + and *
t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)
print(t1 + t2) # Merged
print(t1*3)

# Membership Operator
t1 = (1, 2, 3, 4)

print(1 in t1)
print(1 not in t1)

# Iteration as an loop
t1 = (1, 2, 3, 4)
for i in t1:
    print(i)

# Tuple Functions -->

# len/sum/min/max/sorted
t = (1, 2, 3, 4)
print(len(t))
print(min(t))
print(max(t))
print(sum(t))
print(sorted(t)) # Sorting in form of list
print(sorted(t, reverse=True)) # ASC sorting # Sorting in form of list

# count
t = (1, 2, 3, 4)
print(t.count(3))

# index
t = (1, 2, 3, 4, 1)
print(t.index(1))
#___________________________________________
import time 

L = list(range(100000000))
T = tuple(range(100000000))

start = time.time()
for i in L:
    i*5
print('List time', time.time()-start)

start = time.time()
for i in T:
    i*5
print('Tuple time', time.time()-start)

import sys

L = list(range(1000))
T = tuple(range(1000))

print('List size', sys.getsizeof(L))
print('Tuple size', sys.getsizeof(T))
#_____________________________________________

a = [1, 2, 3]
b = a

a.append(4)
print(a)
print(b)

a = (1, 2, 3, 4)
b = a

a = a + (4,)
print(a)
print(b)

# Tupel unpacing -->
a, b, c = (1, 2, 3)
print(a, b, c)

a, b = (1, 2, 3)
# print(a, b) # Throws an error

# swap values -->
a = 1
b = 2
a, b = b, a
print(a, b)

a, b, *others = (1, 2, 3, 4)
print(a, b)
print(others)

# Zipping tuple -->

a = (1, 2, 3, 4)
b = (5, 5, 7, 8)

print(list(zip(a, b)))
print(tuple(zip(a, b)))

# <--- Sets --->

# Creating sets -->

s = {} # Empty set
print(s)
print(type(s)) # This is not set.

# Right syntex
s = set()
print(s) # This is an empty set.

# 1D set
s1 = {1, 2, 3}
print(s1)

# 2D set
s2 = {2, 3, {1, 2}}
print(s2) # Mutable datatype can not allowed inside of set

# Hetrogenius set
s3 = {'hello', True, 1}
print(s3) # True treated as 1 and set doesn't contains duplicates

s4 = {'hello', True, 1, (1, 2)}
print(s4) # Order doesn't metter in set.

# Type conversion
s4 = set([1, 2, 34])
print(s4)

# Duplicates not allowed
s = {1, 1, 2, 2, 3}
print(s)

# Set can't have mutable items

s = {1, 2, 3, [4, 5]}
# print(s) # Throws an error

# Unordered
s1 = {1, 2, 3}
s2 = {3, 2, 1}
print(s1 == s2) # Output is True because order doesn't metter.

# Accessing items -->

s1 = {1, 2, 3}
print(s1[0]) # Set object is not subscriptable / unordered

# Editing items -->

s1 = {1, 2, 3}
# s1[0] = 100 # Throws an error

# Adding Items -->
s1 = {1, 2, 3}
# add
s1.add(5)
print(s1)
# update
s1.update([5, 6, 7])
print(s1)

# Deleting Items -->

# del
s = {1, 2, 3}
del s
# del s[0] # Throws an error
print(s)

# discard
s1 = {1, 2, 3}
s1.discard(3) # deletes specific item
print(s1)

# remove
s = {1, 2, 3}
s.remove(3)
s.remove(5) # Throws an error because 5 doesn't exists in set
print(s)

# pop
s1 = {1, 2, 3}
s1.pop() # Randomly deletes a item
print(s1)

# clear
s1 = {1, 2, 3}
s1.clear()
print(s1) # empty set

# Operations on sets -->

# Union
s1 = {1, 2, 3}
s2 = {5, 2, 7}
print(s1 | s2)

# Intersection
s1 = {1, 2, 3}
s2 = {5, 2, 7}
print(s1 & s2)

# Difference
s1 = {1, 2, 3}
s2 = {5, 2, 7}
print(s1 - s2)
print(s2 - s1)

# Symmetric difference
s1 = {1, 2, 3}
s2 = {5, 2, 7}
print(s1 ^ s2)

# Membership test -->
s1 = {1, 2, 3}
print(1 in s1)
print(1 not in s1)

# loops -->

s1 = {1, 2, 3}
for i in s1:
    print(i)

# Set Functions -->

# len/min/max/sum/sorted
s = {1, 2, 3}
print(len(s))
print(sum(s))
print(min(s))
print(max(s))
print(sorted(s))
print(sorted(s, reverse=True)) # ASC order

# union/update
s1 = {1, 2, 3}
s2 = {5, 2, 6}
print(s1.union(s2))

s1.update(s2)
print(s1)
print(s2)

# intersection/update
s1 = {1, 2, 3}
s2 = {5, 2, 6}
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)
print(s2)

# diffrence/update
s1 = {1, 2, 3}
s2 = {5, 2, 6}
print(s1.difference(s2))
s1.difference_update(s2)
print(s1)
print(s2)

# symmetric diffrence/update
s1 = {1, 2, 3}
s2 = {5, 2, 6}
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1)
print(s2)

#isdisjoint/issubset/issuperset

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1.isdisjoint(s2)) # Ouput is False because some items is common in both

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5}
print(s2.issubset(s2)) # Output is True because s2's all items present in s1
print(s1.issuperset(s2))

# copy
s1 = {1, 2, 3}
s2 = s1.copy()

print(s1)
print(s2)

# Frozenset -->
# Frozen set is just an immutable version of a Python's set object.
fs1 = frozenset([1, 2, 3])
print(fs1)
fs2 = frozenset([3, 4, 5])
print(fs1.union(fs2))

fs = frozenset([1, 2, frozenset([4, 5])]) # 2D frozen set
print(fs)

# All set's function will works on frozenset also.

# Set Comprehension -->

s = {i for i in range(1, 11)}
print(s)

s = {i for i in range(1, 11) if i > 5}
print(s)

s = {i*i for i in range(1, 11)}
print(s)

# <--- Dictionary --->

# Creating dictionaries
d = {} # Empty dict
print(d)

d = {'name':'lokendra', 'gender':'male'} # 1D Dict also a homogenius dictionary
print(d)

d = {(1, 2, 3):1, 'hello':'world'} # Hetrogenius dictionary
print(d)

s = {
    'name':'lokendra', 
    'college':'bit', 
    'semester':'4th', 
    'subjects':{
        'dsa':50,
        'maths':67,
        'english':34
    }
} # 2D dictionary
print(s)

# Creating dict using dict function
d = dict([(1, 1), (2, 2), (3, 3), ('name', 'lokendra')])
print(d)

d1 = {'name':'lokendra', 'name':'kushwaha'}
print(d1) # keys can not be duplicated

d = {'name':'lokendra', [1, 2, 3]:2}
# print(d) # Throws an error beacuse key not be a mutable datatype

d = {'name':'lokendra', (1, 2, 3):2}
print(d)

# Accessing items -->

my_dict = {'name':'lokendra', 'gender':'male', 'age':30}
# print(my_dict[0]) # Throws an error

my_dict = {'name':'lokendra', 'gender':'male', 'age':20}
print(my_dict['name'])
print(my_dict['age'])

print(my_dict.get('name'))
print(my_dict.get('age'))

s = {
    'name':'lokendra', 
    'college':'bit', 
    'semester':'4th', 
    'subjects':{
        'dsa':50,
        'maths':67,
        'english':34
    }
}
print(s['subjects']['maths'])

# Add new key-value pair -->
d = {'name':'lokendra', 'age':20, 3:3}
d['gender'] = 'male'
d['weight'] = '60'
print(d)

s = {
    'name':'lokendra', 
    'college':'bit', 
    'semester':'4th', 
    'subjects':{
        'dsa':50,
        'maths':67,
        'english':34
    }
}

s['subjects']['ds'] = 89
print(s)

# Remove key-value pairs -->

# pop
d = {'name':'lokendra', 'age':20, 3:3}
d.pop(3)
print(d)

# # pop item
d = {'name':'lokendra', 'age':20, 3:3}
d.popitem() # deletes last key-value pair
print(d)

# del
d = {'name':'lokendra', 'age':20, 3:3}
del d['name']
print(d)

s = {
    'name':'lokendra', 
    'college':'bit', 
    'semester':'4th', 
    'subjects':{
        'dsa':50,
        'maths':67,
        'english':34
    }
}
del s['subjects']['maths']
print(s)

# clear
d = {'name':'lokendra', 'age':20, 3:3}
d.clear()
print(d) # Empty list

# Editing key-value pair -->

s = {
    'name':'lokendra', 
    'college':'bit', 
    'sem':'4th', 
    'subjects':{
        'dsa':50,
        'maths':67,
        'english':34
    }
}
s['sem'] = 5
print(s)
s['subjects']['dsa'] = 60
print(s)

# Dictionary operations -->

# Membership Operator
s = {
    'name':'lokendra', 
    'college':'bit', 
    'semester':'4th', 
    'subjects':{
        'dsa':50,
        'maths':67,
        'english':34
    }
}
print('name' in s)
print('lokendra' not in s)

# loop
d = {'name':'lokendra', 'gender':'male', 'age':20}
for i in d:
    print(i)

for i in d:
    print(i, d[i])

# Dict functions -->

# len/sorted/min/max
d = {'name':'lokendra', 'gender':'male', 'age':20}
print(len(d))
print(sorted(d)) # Output in a list
print(sorted(d, reverse=True)) # Output in a list

# items/keys/value
d = {'name':'lokendra', 'gender':'male', 'age':20}
print(d.items())
print(d.keys())
print(d.values())

# update
d1 = {1:2, 3:4, 4:5}
d2 = {4:7, 6:8}

d1.update(d2)
print(d1)

# Dictionary comprehension -->
d = {i:i**2 for i in range(1, 11)}
print(d)

distances = {'delhi':1000, 'mumbai':2000, 'banglore':3000}
my_dict = {key:value*0.62 for (key, value) in distances.items()}
print(my_dict)

# zip -->
day = ['sunday', 'monday', 'tuesday', 'wed', 'thurs', 'fri', 'sat']
temp_C = [30, 31, 23, 43, 54, 65, 56]

dict = {i:j for (i, j) in zip(day, temp_C)}
print(dict)

# Nested comprehension -->
product = {'phone':10, 'laptop':0, 'charger':32, 'tablet':0}

dict = {key:value for (key, value) in product.items() if value > 0}
print(dict)

d = {
    2:{1:2, 2:4, 3:6, 4:8, 5:10},
    3:{1:3, 2:6, 3:9, 4:12, 5:15},
    4:{1:4, 2:8, 3:12}
}

dict = {i:{j:i*j for j in range(1, 11)} for i in range(2, 5)}
print(dict)
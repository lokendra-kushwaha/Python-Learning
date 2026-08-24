# 🌟 ======================================================================= 🌟
# 🚀                           NAMESPACES & DECORATORS
# 🌟 ======================================================================= 🌟

# 📚 1. NAMESPACES -->
# A namespace is a space that holds names (identifiers). Programmatically speaking, 
# namespaces are strictly Python Dictionaries containing identifiers (keys) and their memory objects (values).

# There are 4 types of namespaces:
# - Built-in Namespace
# - Global Namespace
# - Enclosing Namespace
# - Local Namespace

# 🧠 EXPLANATION: How are Namespaces stored in Memory?
# Python handles everything dynamically using dictionaries. When you create a variable `a = 2`, 
# Python doesn't just put '2' in a box named 'a'. It creates a Dictionary entry.
#
# 📊 RAM (Memory) Architecture Diagram:
# ---------------------------------------------------------
# Global Namespace (Dict) -> locals() or globals()
# {
#    'a': <Memory_Address_0x101> ----> [ Integer Object: 2 ],
#    'temp': <Memory_Address_0x202> -> [ Function Object ]
# }
# ---------------------------------------------------------


# 🗺️ ======================================================================= 🗺️
# 🔍 2. SCOPE AND THE L.E.G.B. RULE
# 🗺️ ======================================================================= 🗺️
# A scope is a textual region of a Python program where a namespace is directly accessible.
# LEGB Rule: The interpreter searches for a name from the inside out:
# 1. Local (L) -> 2. Enclosing (E) -> 3. Global (G) -> 4. Built-in (B)
# If not found anywhere, Python raises a NameError.

# 📌 Case 1: Local and Global
a = 2 # Global variable (Main program level)

def temp():
  b = 3 # Local variable (Inside function)
  print(b)

temp()
print(a)

# 📌 Case 2: Local and Global with the same name
# This is possible because they exist in entirely different dictionary namespaces.
a = 2

def temp2():
  a = 3 # Creates a NEW local variable 'a', doesn't touch the global 'a'
  print(a)

temp2()
print(a)

# 📌 Case 3: Local reading a Global
a = 2

def temp3():
  print(a) 
# Works perfectly. Python checks Local (not found) -> Enclosing (not found) -> Global (FOUND!).

temp3() 
print(a) 


# 📌 Case 4: Editing Global from Local (The Restriction)
a = 2

def temp4():
  # a += 1  # 🚨 Output: UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
  print(a)

# Concept -> We can READ global values from a local scope, but we CANNOT modify them directly.

# 📌 Case 5: The `global` keyword
a = 2

def temp5():
  global a # Tells Python: "Do not create a local 'a'. Directly link to the Global 'a'."
  a += 1
  print(a)

temp5()
print(a)


# 📌 Case 6: Global created inside Local
def temp6():
  global new_global_var 
  new_global_var = 1 # We just injected a variable directly into the Global Namespace from inside a function!
  print(new_global_var)

temp6()
print(new_global_var) 


# 📌 Case 7: Function parameters are ALWAYS Local
def temp7(z):
  print(z)

a = 5
temp7(5)
print(a)
# print(z) # 🚨 Error: 'z' is a local parameter. It was destroyed as soon as the function ended.


# 🏛️ ======================================================================= 🏛️
# 🏛️ 3. BUILT-IN SCOPE
# 🏛️ ======================================================================= 🏛️
import builtins
print(dir(builtins)) # Shows all built-in functions (print, max, min, type, etc.)

# Renaming built-ins
L = [1,2,3]
print(max(L)) # Works perfectly here.

# 🧠 EXPLANATION: Python vs. Compiled Languages (C/Java)
# Question: "If this was C/Java, wouldn't it throw an error immediately? Why did `max()` work above but crash below?"
# Answer: Exactly! C and Java are COMPILED. The compiler reads the entire file at once. If you overwrite a built-in keyword, the compiler fails immediately before the program even runs.
# Python is INTERPRETED. It executes line-by-line. 
# At line 124, `max` is not in the Global scope yet, so Python falls back to the Built-in scope and works!
# At line 133, you created a new Global variable called `max` pointing to your custom function. 
# The next time you call `max()`, the LEGB rule stops at Global (it never reaches Built-in!). Since your custom `max` takes 0 arguments, it crashes.

def max():
  print('hello')

# print(max(L)) # 🚨 Output -> TypeError: max() takes 0 positional arguments but 1 was given


# 📦 ======================================================================= 📦
# 📦 4. ENCLOSING SCOPE & NONLOCAL KEYWORD
# 📦 ======================================================================= 📦
# 🧠 EXPLANATION: What is Enclosing Scope?
# When you have a function INSIDE another function (Nested Functions), the outer function's scope acts as a middle-ground. It is not Global, but it is not Local to the inner function either. We call this the "Enclosing Scope".

def outer():
  def inner():
    print('Inner Function (Local Scope)')
  
  inner()
  print('Outer Function (Enclosing Scope)')

outer()
print('Main program (Global Scope)')


# Scenario A: Found in Local
def outer2():
  a = 3
  def inner2():
    a = 4
    print(a) # Prints 4 (Found in Local)
  inner2()

a = 1
outer2()


# Scenario B: Found in Enclosing
def outer3():
  a = 3
  def inner3():
    print(a) # Prints 3 (Not in Local -> Found in Enclosing)
  inner3()

a = 1
outer3()


# Scenario C: Found in Global
def outer4():
  def inner4():
    print(a) # Prints 1 (Not Local -> Not Enclosing -> Found in Global)
  inner4()

a = 1
outer4()


# 📌 The `nonlocal` keyword
def outer5():
  a = 1
  def inner5():
    nonlocal a # Tells Python: "I want to modify the variable from the Enclosing scope!"
    a += 1 
    print('inner',a)
  inner5()
  print('outer',a)

outer5()


# 🎭 ======================================================================= 🎭
# 🪄 5. DECORATORS & CLOSURES (Advanced Architecture)
# 🎭 ======================================================================= 🎭

# A decorator in python is a function that receives another function as input, adds some 
# functionality (decoration) to it, and returns it.
# This can happen ONLY because Python functions are "1st Class Citizens".

# 🧠 EXPLANATION: What is a "First-Class Citizen"?
# In programming, an entity is a "First-Class Citizen" if it can be:
# 1. Assigned to a variable (`a = func`)
# 2. Passed as an argument to another function (`modify(func)`)
# 3. Returned from a function (`return func`)
# In Python, Functions are treated exactly like Integers, Strings, or Lists. They are Objects in memory!

def func():
  print('hello')

a = func # Assigning function to a variable (No brackets!)
a()      
# del a  # We can even delete it!

def modify(func, num):
  return func(num)

def square(num):
  return num**2

print(modify(square, 2))


# 📌 Simple example of Decorator
def my_decorator(func):
    def wrapper(): 
        print('***********************')
        func()
        print('***********************')
    return wrapper

def hello():
    print('hello')

a = my_decorator(hello)
a()


# 🧠 EXPLANATION: CLOSURES (How does this actually work in memory?)
# Question: "If the parent function dies, how does the child function access its variables?"
# Answer: Normally, when a function returns, its local namespace is completely destroyed by the Garbage Collector.
# HOWEVER, Python has a special feature called a "Closure". 
# If an Inner function (`wrapper`) uses a variable from its Enclosing function (`func`), and that Inner function is returned, Python creates a "Closure". 
# Think of a Closure as a Backpack 🎒. When `my_decorator` dies, it packs the `func` variable into a backpack and ties it to the `wrapper` function. 
# Even though the parent is dead, the child still carries the exact memory state it needs in its `__closure__` attribute!


# 📌 Better Syntax? -> The Syntactic Sugar (@)
@my_decorator
def hello2():
  print('hello using @')

hello2()


# 📌 Meaningful Example: Execution Timer
import time

def timer(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    print(f"Time taken by {func.__name__}: {time.time()-start} secs.")
    return result
  return wrapper

@timer
def heavy_task():
  print('Running heavy task...')
  time.sleep(1)

heavy_task()


# 📌 Decorators with Arguments (The 3-Level Nesting)
def sanity_check(data_type):
  def outer_wrapper(func):
    def inner_wrapper(*args):
        
      # 🧠 EXPLANATION: The `*args` Unpacking Mystery
      # Question: "Why did type(*args) work, but type(args) didn't? And why use args[0]?"
      # Answer: `args` is ALWAYS a Tuple. If you call `square(2)`, `args` is `(2,)`.
      # If you check `type(args) == int`, it will FAIL because `type((2,))` is a `tuple`.
      # 
      # When you do `type(*args)`, the `*` unpacks the tuple. 
      # So `type(*(2,))` becomes `type(2)`, which evaluates to `int`. THIS WORKS!
      # BUT, if your function has multiple arguments like `power(2, 3)`, `args` is `(2, 3)`.
      # Unpacking it makes `type(*(2, 3))` -> `type(2, 3)`. Python's `type()` function throws an ERROR if you give it exactly two arguments!
      #
      # SOLUTION: `args[0]` specifically looks at the FIRST parameter passed. It is the safest way to check the data type of the primary argument without unpacking errors!

      if type(args[0]) == data_type: 
        return func(*args)
      else:
        raise TypeError(f'Invalid Data Type! Expected {data_type}, got {type(args[0])}')
        
    return inner_wrapper
  return outer_wrapper


@sanity_check(int)
def calculate_square(num):
  print(num**2)

@sanity_check(str)
def greet(name):
  print('Hello', name)

calculate_square(2)
greet('Lokendra')

# 🌟 ======================================================================= 🌟
#                  END OF NAMESPACES & DECORATORS MASTERCLASS
# 🌟 ======================================================================= 🌟
# 🌟 ======================================================================= 🌟
# 🚀                        RECURSION & MEMOIZATION
# 🌟 ======================================================================= 🌟

# 💡 CONCEPT: Recursion is a technique where a function calls itself to solve a smaller instance of the same problem.
# Benefit -> Eliminates the need for complex loops and makes mathematical/tree-based problems easier to write.

# 🔄 ======================================================================= 🔄
# 1. ITERATION VS RECURSION (The Multiplication Example)
# 🔄 ======================================================================= 🔄

# Code by iteration/loop -->
def multiply_loop(a, b):
    result = 0
    for i in range(0, b):
        result = result + a
    print(result)

multiply_loop(3, 4)

# Code by recursion --> 
# We must focus on 2 things:
# 1. Base Case: The condition where the recursion stops (the known value).
# 2. Recursive Step: How to break the main problem down into a smaller problem.

def mul(a, b):
    if b == 1:       # Base Case
        return a
    else:            # Recursive Step
        return a + mul(a, b-1)

print(mul(5, 6))

# 🧠 EXPLANATION: How does this work & What is the Return Chain?
# When you call `mul(5, 3)`, it doesn't calculate the answer immediately. It builds a chain of deferred operations.
# 
# Step 1: mul(5, 3) -> returns 5 + mul(5, 2)  (Waiting for mul(5,2))
# Step 2: mul(5, 2) -> returns 5 + mul(5, 1)  (Waiting for mul(5,1))
# Step 3: mul(5, 1) -> Hits the Base Case! Returns 5.
# 
# Now the chain resolves backwards (The Return Chain):
# mul(5, 1) gives 5  -> mul(5, 2) becomes 5 + 5 = 10
# mul(5, 2) gives 10 -> mul(5, 3) becomes 5 + 10 = 15. Final Answer!


# 💥 ======================================================================= 💥
# 2. THE FACTORIAL BATTLE: LOOP VS RECURSION (Memory Limits)
# 💥 ======================================================================= 💥

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
    
# print(fact(999)) # Works, but fact(1000) will throw RecursionError!

total = 1
for i in range(1, 1559): # Notice we must start from 1, not 0, otherwise total becomes 0!
    total = total * i
# print(total) # Loops can easily handle 1558 and even 100,000 without crashing!

# 🧠 EXPLANATION: Why did Recursion crash at 1000 while the Loop survived?
# Observation: "I am surprised! Are loops more powerful than recursion?"
# Answer: YES, in terms of memory efficiency, loops are far superior. Here is the technical reason:
# 
# 1. The Loop Memory: A `for` loop executes inside a SINGLE memory block (Stack Frame). It just overwrites the `total` variable again and again. Space complexity is O(1).
# 2. The Recursion Call Stack: Every time a function calls itself, the Operating System pauses the current function and creates a brand NEW memory block (Stack Frame) on top of the old one to store the new local variables. 
# 
# If you call `fact(1000)`, Python literally builds a tower of 1,000 memory blocks stacked on top of each other in the RAM. 
# To prevent your entire computer's RAM from overflowing and crashing, Python has a built-in safety lock (`sys.getrecursionlimit()`) set to 1000. When the tower hits 1000 blocks, Python throws a `RecursionError` and shuts it down.


# 🎭 ======================================================================= 🎭
# 3. STRING RECURSION (Palindrome Checker)
# 🎭 ======================================================================= 🎭

def palindrome(text):
    if len(text) <= 1:           # Base Case
        print("Palindrome")
    else:
        if text[0] == text[-1]:  # Check first and last character
            palindrome(text[1:-1]) # Pass the string without first and last characters
        else:
            print("Not a palindrome")

palindrome("madam")
palindrome("lokendra")
palindrome("laal")


# 🐇 ======================================================================= 🐇
# 4. THE FIBONACCI (RABBIT) PROBLEM & TIME COMPLEXITY
# 🐇 ======================================================================= 🐇

import time

def fibonacci(month):
    if month == 0 or month == 1:
        return 1
    else:
        return fibonacci(month - 1) + fibonacci(month - 2)

start = time.time()
print(f"Fibonacci Answer: {fibonacci(12)}") # Try putting 35 here, your PC will freeze!
print(f"Time Taken (Normal): {time.time() - start} seconds")

# 🧠 EXPLANATION: Why is this so slow? (Exponential Time Complexity)
# Because to find one Fibonacci number, you have to calculate the previous two. 
# This creates a massive, repetitive tree where the exact same calculations are done thousands of times!
#
# 🌳 ASCII Recursion Tree for fib(4):
#                  fib(4)
#                /        \
#          fib(3)          fib(2)
#          /    \          /    \
#     fib(2)   fib(1)  fib(1)  fib(0)
#     /    \
#  fib(1) fib(0)
#
# Notice how `fib(2)` is calculated TWICE. If we do `fib(40)`, `fib(2)` is calculated millions of times!
# Time Complexity: O(2^n) -> For every step, the branches double. 


# 🛡️ ======================================================================= 🛡️
# 5. DYNAMIC PROGRAMMING: MEMOIZATION (The Ultimate Fix)
# 🛡️ ======================================================================= 🛡️
# Concept: Space-Time Trade-off. We sacrifice some RAM (Space) to drastically save Processing Power (Time).

# 🧠 EXPLANATION: What is Memoization? (Technical & Simple Language)
# Simple Language: Imagine you are asked "What is 584 x 783?". You spend 2 minutes calculating it and say "457,272". 
# If someone asks you the exact same question 5 seconds later, do you calculate it again? NO! You just remember the answer.
# 
# Technical Language: Memoization is a caching technique used in Dynamic Programming. We use a Hash Map (Python Dictionary) to store the results of expensive function calls. Before executing a recursive call, we check the Hash Map. If the answer exists, we return it in O(1) time, entirely skipping the massive calculation tree.

def memo_fib(m, d): 
    if m in d:               # Checking the cache (Dictionary)
        return d[m]          # Returning saved answer instantly! O(1)
    else:
        # If not calculated yet, calculate it, SAVE it in dict, then return it.
        d[m] = memo_fib(m-1, d) + memo_fib(m-2, d)
        return d[m]

start = time.time()
cache_dict = {0: 1, 1: 1} # Base cases pre-loaded in the cache
print(f"Fibonacci Memoization Answer: {memo_fib(50, cache_dict)}")
print(f"Time Taken (Memoized): {time.time() - start} seconds")

# 🧠 EXPLANATION: Complexity Comparison (Before vs After)
# 🔴 BEFORE (Normal Recursion):
# - Time Complexity: O(2^n) (Exponential - Graph shoots straight up like a rocket).
# - Space Complexity: O(n) (Call Stack limit).
#
# 🟢 AFTER (Memoization):
# - Time Complexity: O(n) (Linear - We only calculate each number EXACTLY ONCE).
# - Space Complexity: O(n) + O(n) = O(n) (Call Stack + Dictionary Memory). We used a little more RAM, but saved hours of processing time!

# 📈 The Time Complexity Graph (ASCII)
# ​Here is the visual representation of why O(2^n) (Normal Recursion) is dangerous, and why Memoization O(n) is required in Data Science

# Time Taken
#     ^
#     |                                    * (O(2^n) - Normal Recursion)
#     |                                   *  <-- Your CPU freezes here
#     |                                 *
#     |                               *
#     |                             *
#     |                           *
#     |                         *
#     |                       *
#     | - - - - - - - - - - * - - - - - - - - - (Time Limit Exceeded)
#     |                  *
#     |               *
#     |      * * * * * * * * * * * * * * * * * * (O(n) - Memoization)
#     | * * 
#     +-----------------------------------------> Input Size (n)


# 🧩 ======================================================================= 🧩
# 6. CREATING A POWER SET (Generating Subsets)
# 🧩 ======================================================================= 🧩
# Note: A Power Set means finding all possible combinations of a list.

def power_set(lst):
    if len(lst) == 0:  # Base case: empty list returns a list containing an empty list
        return [[]]
    else:
        first_element = lst[0]
        # Recursively find subsets of the remaining list
        subsets_without_first = power_set(lst[1:])
        
        # Add the first element to all those subsets
        subsets_with_first = []
        for subset in subsets_without_first:
            subsets_with_first.append([first_element] + subset)
            
        # Combine and return
        return subsets_without_first + subsets_with_first
    
print(f"Power Set: {power_set([1, 2, 3])}")

# 🌟 ======================================================================= 🌟
#                       END OF RECURSION MASTERCLASS
# 🌟 ======================================================================= 🌟
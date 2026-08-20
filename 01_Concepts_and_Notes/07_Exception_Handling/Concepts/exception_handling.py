# 🌟 ======================================================================= 🌟
# 🚀                            EXCEPTION HANDLING
# 🌟 ======================================================================= 🌟

# 💡 CONCEPT: There are 2 stages where an error may happen in a program:
# 1. During compilation -> Syntax Error
# 2. During execution -> Exceptions


# 🛑 ======================================================================= 🛑
# ❌ 1. SYNTAX ERRORS (Grammar Mistakes)
# 🛑 ======================================================================= 🛑
# - Something in the program is not written according to the programming grammar.
# - The error is raised by the interpreter/compiler.
# - You can solve it by rectifying the code syntax.

# Examples of syntax error:
# print 'hello world'
# 🚨 Output -> SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

# Other examples of syntax error:
# - Leaving out symbols like colons or brackets
# - Misspelling a keyword
# - Incorrect indentation
# - Empty if/else/loops/class/functions without a 'pass' statement

# a = 5
# if a==3
#   print('hello')
# 🚨 Output : SyntaxError: expected ':'

# a = 5
# if a==3:
# print('hello')
# 🚨 Output : IndentationError: expected an indented block after 'if' statement


# 💥 ======================================================================= 💥
# ⚠️ 2. BUILT-IN EXCEPTIONS (Runtime Errors)
# 💥 ======================================================================= 💥

# 📌 IndexError: Thrown when trying to access an item at an invalid index.
# L = [1,2,3]
# L[100]
# 🚨 Output : IndexError: list index out of range

# 📌 ModuleNotFoundError: Thrown when a module could not be found.
# import mathi
# math.floor(5.3)
# 🚨 Output : ModuleNotFoundError: No module named 'mathi'

# 📌 KeyError: Thrown when a dictionary key is not found.
# d = {'name':'nitish'}
# d['age']
# 🚨 Output : KeyError: 'age'

# 📌 TypeError: Thrown when an operation is applied to an object of an inappropriate type.
# 1 + 'a'
# 🚨 Output : TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 📌 ValueError: Thrown when a function's argument is of an inappropriate type (but right category).
# int('a')
# 🚨 Output : ValueError: invalid literal for int() with base 10: 'a'

# 📌 NameError: Thrown when an object/variable could not be found in memory.
# print(k)
# 🚨 Output : NameError: name 'k' is not defined

# 📌 AttributeError: Thrown when an attribute/method doesn't exist for that object.
# L = [1,2,3]
# L.upper()
# 🚨 Output : AttributeError: 'list' object has no attribute 'upper'

# 📜 Stacktrace: The detailed technical report Python prints showing exactly which line caused the error.


# 🛡️ ======================================================================= 🛡️
# 🏗️ EXCEPTION HANDLING (The Safety Net)
# 🛡️ ======================================================================= 🛡️
# This handles situations where things go wrong during the execution of the program (runtime). 
# It generally happens due to unforeseen circumstances.
# - Exceptions are raised by the Python runtime.
# - You have to tackle them on the fly.

# **Examples:**
# - Memory overflow
# - Divide by 0 -> Logical error
# - Database connection error

# 🧠 EXPLANATION: Why is it crucial to handle exceptions?
# 1. User Experience (UX): If an app crashes and displays a massive red error block, the user might delete the app. Handling exceptions allows us to show a friendly message instead (e.g., "Something went wrong, please try again").
# 2. Security: When an unhandled error occurs, Python prints the entire 'Stacktrace'. This exposes your file names, folder paths, and server architecture. Hackers exploit this technical information to breach systems. Catching errors manually hides this sensitive data!

# How to handle exceptions -> The Try-Except block

# Let's create a file for testing
with open('Python/sample.txt','w') as f:
  f.write('hello world')

# Try-except demo -->
try:
    with open('sample.txt','r') as f:
        print(f.read())
except:
    print('Sorry, the file was not found.')


# 🎯 Catching Specific Exceptions (Industry Best Practice)
try:
    m = 5
    f = open('sample.txt','r')
    print(f.read())
    print(m)
    print(5 / 2)
    L = [1, 2, 3]
    L[100]

except FileNotFoundError:
    print('Error: File not found in the directory.')
except NameError:
    print('Error: Variable is not defined.')
except ZeroDivisionError:
    print("Error: Cannot divide a number by zero.")
except Exception as e: # Default catcher for any unknown error
    print(f"An unexpected error occurred: {e}")
    print(e.with_traceback)


# 🚦 ======================================================================= 🚦
# 🔄 THE 'ELSE' AND 'FINALLY' BLOCKS
# 🚦 ======================================================================= 🚦

# 🧠 EXPLANATION: When and why do we use 'else'?
# Rule: The 'try' block should ONLY contain code that has a risk of crashing. 
# If the code inside the 'try' block executes 100% successfully (without any errors), ONLY THEN will the 'else' block execute. 
# This separates the risky code from the safe execution logic.
try:
    f = open('Python/sample.txt', 'r')
except FileNotFoundError:
    print('File not found')
except Exception:
    print('An error occurred')
else:
    print(f.read()) # Executes ONLY if the file was successfully opened


# 🧠 EXPLANATION: When and why do we use 'finally'?
# The 'finally' block executes NO MATTER WHAT (whether an error occurs, the code succeeds, or the program returns early).
# It is strictly used for "Resource Cleanup". 
# Example: If you open a Database connection, and the code crashes halfway through, the database remains vulnerable and locked. 
# Placing `db.close()` or `file.close()` inside the 'finally' block guarantees that the connection is safely closed under all circumstances.
try:
  f = open('sample1.txt','r')
except FileNotFoundError:
  print('File not found')
except Exception:
  print('Something went wrong')
else:
  print(f.read())
finally:
  print('This will print regardless of success or failure (Cleanup complete!)')


# 🚀 ======================================================================= 🚀
# 🛠️ RAISE (Manually Throwing Exceptions)
# 🚀 ======================================================================= 🚀
# In Python programming, exceptions are automatically raised when errors occur at runtime. 
# However, we can also manually trigger exceptions using the `raise` keyword.

# We can optionally pass string values to the exception to clarify why it was raised.
# Benefit -> Raising an error allows the except block to catch it, which is perfect for enforcing strict Business Logic.

# raise ZeroDivisionError('Just testing the raise keyword')

# 💡 Concept mapping with Java:
# Python `try`    -> Java `try`
# Python `except` -> Java `catch`
# Python `raise`  -> Java `throw`

class Bank:
  def __init__(self, balance):
    self.balance = balance

  def withdraw(self, amount):
    if amount < 0:
        raise Exception('Amount cannot be negative.')
    if self.balance < amount:
        raise Exception('Insufficient balance.')
    self.balance = self.balance - amount

obj = Bank(10000)
try:
    obj.withdraw(15000)
except Exception as e:
    print(f"Transaction Failed: {e}")
else:
    print(f"Remaining Balance: {obj.balance}")


# 👑 ======================================================================= 👑
# 🧑‍💻 CREATING YOUR OWN CUSTOM EXCEPTIONS
# 👑 ======================================================================= 👑

# When we create our own custom exception class, we MUST inherit it from Python's base `Exception` class. 
# If we don't inherit it, Python won't allow us to use the `raise` keyword on it.

class MyException(Exception): 
  def __init__(self, message):
    print(message)

class Bank2:
  def __init__(self, balance):
    self.balance = balance

  def withdraw(self,amount):
    if amount < 0:
       raise MyException('Amount cannot be negative.')
    if self.balance < amount:
       raise MyException('Insufficient balance.')
    self.balance = self.balance - amount

obj2 = Bank2(10000)
try:
   obj2.withdraw(5000)
except MyException as e:
   pass # The error message is already printed inside the custom exception's __init__
else:
   print(f"Balance: {obj2.balance}")


# 🧠 EXPLANATION: Why do we need to build Custom Exceptions?
# Benefit -> FULL ARCHITECTURAL CONTROL!
# A normal built-in 'Exception' just prints a text message. But a Custom Exception is a full Class!
# This means we can add our own specific methods inside it (like `logout()`, `send_alert_to_admin()`, or `block_ip()`).
# So, if a hacker inputs the wrong password, we don't just throw an error; our Custom Exception can actively trigger a security protocol to ban their device!

class SecurityError(Exception):
  def __init__(self, message):
    print(f"SECURITY ALERT: {message}")

  def logout(self):
    print('Action: User forcibly logged out due to a security breach!')

class Google:
  def __init__(self, name, email, password, device):
    self.name = name
    self.email = email
    self.password = password
    self.device = device

  def login(self, email, password, device):
    if device != self.device:
       raise SecurityError('Unrecognized device attempting access!')
    if email == self.email and password == self.password:
       print('Welcome, login successful.')
    else:
       print('Login error: Invalid credentials.')


obj3 = Google('Lokendra', 'lokendra@gmail.com', '1234', 'android')

print("\n--- Google Security Test ---")
try:
   # Simulating a hacker trying to login from a different device (windows)
   obj3.login('lokendra@gmail.com', '1234', 'windows')
except SecurityError as e:
   e.logout() # Calling the custom defense method from our exception class!
else:
   print(f"Logged in as: {obj3.name}")
finally:
   print('Database connection closed safely.')

# 🌟 ======================================================================= 🌟
#                           END OF EXCEPTION HANDLING
# 🌟 ======================================================================= 🌟
# 🌟 ======================================================================= 🌟
# 🚀                        OOPs --> CLASS RELATIONSHIPS
# 🌟 ======================================================================= 🌟

# 💡 CONCEPT: Class Relationships -->
# 1. Aggregation (Has-A relationship)
# 2. Inheritance (Is-A relationship)


# 🔗 ======================================================================= 🔗
# 🏢 1. AGGREGATION ("Has-A" Relationship)
# 🔗 ======================================================================= 🔗
# Meaning: One class "Owns" the other class. 
# Ex. -> class Customer, class Address --> Customer Has an Address (Customer class owns Address class)

class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address # Complex entity (Home address, Landmark, Pin etc. passed as an Object)

    def print_address(self):
        # print(self.address.city, self.address.pin, self.address.state) # This worked when city was NOT a private variable.
        print(self.address.get_city(), self.address.pin, self.address.state) # Using Getter for private var.

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.edit_address(new_city, new_pin, new_state)


class Address:
    def __init__(self, city, pin, state):
        self.__city = city # 🚨 Private variable
        self.pin = pin
        self.state = state

    def get_city(self):
        return self.__city
    
    def edit_address(self, new_city, new_pin, new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state

print("--- Aggregation Output ---")
add1 = Address('Orai', '285001', 'Uttarpradesh')
cust = Customer('lokendra', 'male', add1)

cust.print_address() 

# 🧠 UNDER THE HOOD: What about private variables in Aggregation?
# If we make the 'city' variable private in the Address class, and try to access it via `self.address.city`:
# Output => 'Address' object has no attribute 'city'
# 🎯 CONCLUSION: One class CANNOT access the private variables of another class directly, even in Aggregation.
# Solution: We use a `getter` method in the Address class so the Customer class can fetch the private variable securely.

cust.edit_profile('vivek', 'mumbai', '111111', 'maharastra')
cust.print_address() # After setting up edit_address, no error will occur because we permitted it.
print("-" * 40)


# 🧬 ======================================================================= 🧬
# 👨‍👦 2. INHERITANCE ("Is-A" Relationship)
# 🧬 ======================================================================= 🧬
# What is the benefit? --> Code Reusability!

# Parent class
class User:
    def __init__(self):
        self.name = 'lokendra'

    def login(self):
        print('Login Successful')

# Child class
class Student(User):
    # def __init__(self):
    #     self.rollno = 100

    def enroll(self):
        print('Enrolled into the course.')

print("--- Inheritance Output ---")
u = User()
s = Student()
print(s.name)

# 💡 CONCEPT: Constructor Overriding
# If both Child and Parent classes have their own constructors (__init__), ONLY the Child class constructor will be called.
# This is called Method Overriding / Constructor Overriding.

s.login()
s.enroll()
print("-" * 40)


# 🧳 ======================================================================= 🧳
# ❓ WHAT GETS INHERITED?
# 🧳 ======================================================================= 🧳
# 1. Constructor
# 2. Non-Private Attributes
# 3. Non-Private Methods

# --- Example 1: Constructor Inheritance ---
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    pass # Child has no constructor

print("--- Constructor Inheritance ---")
s = SmartPhone(20000, "Apple", 13) 
# 🎯 CONCLUSION: If the child class does not have its own constructor, the parent class constructor is automatically called.
s.buy()


# --- Example 2: Constructor Overriding ---
class Phone2:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone2(Phone2):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print("Inside SmartPhone constructor")

print("\n--- Constructor Overriding ---")
s2 = SmartPhone2("Android", 2) 
# 🎯 CONCLUSION: Now the child's constructor will be used because it has its own. 
# s2.brand # 🚨 Throws an error! Because the parent's constructor was NEVER executed, so 'brand' was never initialized.


# 🚫 ======================================================================= 🚫
# 🔒 PRIVATE MEMBERS IN INHERITANCE
# 🚫 ======================================================================= 🚫
# 💡 CONCEPT: A Child CANNOT access private members of the Parent class directly.

class Phone3:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price # Private
        self.brand = brand
        self.camera = camera

    # acting as a getter
    def __show(self): # Private Method
        print(self.__price)

class SmartPhone3(Phone3):
    def check(self):
        print(self.__price)

s3 = SmartPhone3(20000, "Apple", 13)
# s3.check() # 🚨 Output -> 'SmartPhone3' object has no attribute '_SmartPhone3__price'. 
# Because the child class cannot access the parent class's private attribute.
# Way to access it -> Use a Getter in the parent class!

# s3.__show() # 🚨 Output -> 'SmartPhone3' object has no attribute '__show' 
# Because a child class cannot access private methods either!


# ✅ The Correct Way to Access Parent's Private Data
class Parent:
    def __init__(self, num):
        self.__num = num

    # acting as a getter
    def get_num(self):
        return self.__num

class Child(Parent):
    def show(self):
        print("This is in child class")

print("\n--- Accessing Parent's Private Data via Getter ---")
son = Child(100)
print(son.get_num()) # Output --> 100
son.show()           # Output --> This is in child class


# 🚨 The Constructor Trap
class Parent2:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num

class Child2(Parent2):
    def __init__(self, val, num):
        self.__val = val # We overrode the constructor, so Parent's __init__ never ran!

    def get_val(self):
        return self.__val
        
son2 = Child2(100, 10)
# print("Parent: Num:", son2.get_num()) # 🚨 Output -> 'Child2' object has no attribute '_Parent2__num'. Why? Because the parent constructor never ran!
print("Child: Val:", son2.get_val())


# 🔄 ======================================================================= 🔄
# ⚔️ VARIABLE & METHOD OVERRIDING
# 🔄 ======================================================================= 🔄

class A:
    def __init__(self):
        self.var1 = 100

    def display1(self, var1): 
        # var1 (local argument) is NOT utilized here, we updated self.var1
        self.var1 = var1 
        print("class A :", self.var1)

class B(A):
    def display2(self, var1):
        print("class B :", self.var1)

print("\n--- Variable Modification Flow ---")
obj = B()
obj.display1(200) # Output -> class A : 200 (Because display1 modifies self.var1 to 200)


# --- Method Overriding ---
class Phone4:
    def __init__(self, price, brand, camera):
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone4(Phone4):
    def buy(self):
        print("Buying a smartphone")

print("\n--- Method Overriding ---")
s4 = SmartPhone4(20000, "Apple", 13)
s4.buy() 
# 🎯 CONCLUSION: If the exact same method exists in both Child and Parent, the Child class's method will execute. This is Method Overriding.


# 🦸‍♂️ ======================================================================= 🦸‍♂️
# 🔑 THE SUPER() KEYWORD
# 🦸‍♂️ ======================================================================= 🦸‍♂️

class Phone5:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone5(Phone5):
    def buy(self):
        print("Buying a smartphone")
        # syntax to call -> parent's buy method
        super().buy()

print("\n--- Super Keyword ---")
s5 = SmartPhone5(20000, "Apple", 13)
s5.buy() 
# Output -> Buying a smartphone
#           Buying a phone


# --- Super() to call Parent Constructor ---
class Phone6:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone6(Phone6):
    def __init__(self, price, brand, camera, os, ram):
        print('Inside smartphone constructor (Start)')
        super().__init__(price, brand, camera) # Triggers Parent Setup!
        self.os = os
        self.ram = ram
        print("Inside smartphone constructor (End)")

print("\n--- Super Keyword (Constructor Flow) ---")
s6 = SmartPhone6(20000, "Samsung", 12, "Android", 2)
print(s6.os)
print(s6.brand)


# 🚫 CAN SUPER() ACCESS PARENT'S DATA VARIABLES?
class SmartPhone7(Phone5):
    def buy(self):
        print("Buying a smartphone")
        # print(super().brand) # 🚨 'super' object has no attribute 'brand' 
        # Meaning: We can ONLY access Methods using super(), NOT attributes!

# super().buy() # 🚨 Output -> RuntimeError: super(): no arguments -> Cannot use super keyword outside the class.

# 🎯 CONCLUSIONS ON SUPER():
# 1. super() cannot access variables/attributes. (Because variables belong to `self`, methods belong to the Class).
# 2. super() cannot be used outside the class.
# 3. super() is primarily used in child classes to invoke overridden parent methods or constructors.


# 🌳 ======================================================================= 🌳
# 📊 TYPES OF INHERITANCE
# 🌳 ======================================================================= 🌳

# 1. Single Inheritance ---> One Parent, One Child
class SmartPhoneSingle(Phone):
    pass

# 2. Multilevel Inheritance ---> Grandfather -> Father -> Child
class ProductMulti:
    def review(self):
        print("Product customer review")

class PhoneMulti(ProductMulti):
    def buy(self):
        print("Buying a phone")

class SmartPhoneMulti(PhoneMulti):
    pass

print("\n--- Multilevel Inheritance ---")
sm = SmartPhoneMulti()
sm.buy()
sm.review() # Child can access everything upwards in the chain!

# 3. Hierarchical Inheritance ---> One Parent -> Multiple Children
class FeaturePhone(Phone):
    pass
# Here both SmartPhone and FeaturePhone inherit from Phone.

# 4. Multiple Inheritance ---> Multiple Parents -> One Child
class PhoneMultiple:
    def buy(self):
        print("Buying a phone")

class ProductMultiple:
    def review(self):
        print("Customer review")

class SmartPhoneMultiple(PhoneMultiple, ProductMultiple):
    pass

print("\n--- Multiple Inheritance ---")
s_multi = SmartPhoneMultiple()
s_multi.buy()
s_multi.review()


# 💎 ======================================================================= 💎
# 🚨 THE DIAMOND PROBLEM (Method Resolution Order - MRO)
# 💎 ======================================================================= 💎

class PhoneDiamond:
    def buy(self):
        print("Phone buy method")

class ProductDiamond:
    def buy(self):
        print("Product buy method")

class SmartPhoneDiamond(PhoneDiamond, ProductDiamond):
    pass

print("\n--- The Diamond Problem (MRO) ---")
s_diamond = SmartPhoneDiamond()
s_diamond.buy() # Output: "Phone buy method"

# 🧠 UNDER THE HOOD: Why did it print "Phone buy method" and not "Product buy method"?
# EXPLANATION:
# When multiple parents have the same method (like `buy()`), Python gets confused. 
# To solve this, Python uses MRO (Method Resolution Order) based on the C3 Linearization Algorithm.
# Rule: It reads the inheritance tuple from LEFT to RIGHT.
# In `class SmartPhoneDiamond(PhoneDiamond, ProductDiamond):`, `PhoneDiamond` is on the left.
# So, it checks PhoneDiamond first. If it finds `buy()`, it executes it and stops looking further!


# 🎭 ======================================================================= 🎭
# 🦄 POLYMORPHISM (Many Forms)
# 🎭 ======================================================================= 🎭
# - Method Overriding (Done above)
# - Method Overloading
# - Operator Overloading

# 1. Method Overloading -->
# Benefit: Code is cleaner to read. Same method name handles different amounts of arguments.
class Shape:
    def area(self, a, b=0): # Method overloading workaround in Python
        if b == 0:
            return 3.14 * a * a # Acts as area of circle
        else:
            return a * b        # Acts as area of rectangle
    
    # def area(self, l, b): 
    #     return l * b
    # 🚨 If we write two methods with the SAME name, Python forgets the first one and only keeps the latest one!
    # Output -> TypeError: Shape.area() missing 1 required positional argument: 'b'
    
    # 🎯 CONCLUSION: True Method Overloading (like in Java or C++) DOES NOT EXIST in Python. 
    # Because Python is dynamically typed, it doesn't care about parameter types. We handle it using default arguments (b=0) or *args.

print("\n--- Method Overloading (Workaround) ---")
shape_obj = Shape()
print(shape_obj.area(2))    # Runs Circle Logic
print(shape_obj.area(3, 4)) # Runs Rectangle Logic

# 2. Operator Overloading -->
# Meaning: The exact same operator behaves differently depending on the input data types.
# This happens under the hood using "Magic Methods" (like __add__).

print("\n--- Operator Overloading ---")
print('hello' + 'world')   # + operator works as String Concatenation
print(4 + 5)               # + operator works as Mathematical Addition
print([1, 2, 3] + [4, 5])  # + operator works as List Merging


# 🛡️ ======================================================================= 🛡️
# 🏛️ ABSTRACTION (Hiding implementation details & Enforcing Rules)
# 🛡️ ======================================================================= 🛡️
# Meaning of word -> Hidden
# 💡 CONCEPT: The Main class can apply constraints on the lower classes (to ensure that child classes obey our rules).

from abc import ABC, abstractmethod # ABC -> Abstract Base Class module

# Abstract class -> A class that has at least one abstract method.
class BankApp(ABC): # It becomes an Abstract Class ONLY when it inherits from ABC.

    def database(self):
        print('Connected to database!')

    @abstractmethod # This decorator means this method will have NO code here, BUT child classes MUST implement it.
    def security(self):
        pass

    @abstractmethod
    def display(self):
        pass

class MobileApp(BankApp):
    def mobile_login(self):
        print('Logged into mobile')

    # If we do NOT implement this security method, we get an error:
    # 🚨 TypeError: Can't instantiate abstract class MobileApp without an implementation for abstract method 'security'
    def security(self): 
        print('Mobile Security Protocol Activated') # Obeying the Rule!

    def display(self): 
        print('Displaying UI')

print("\n--- Abstraction ---")
mob = MobileApp()
mob.mobile_login()
mob.security()

# obj = BankApp() # 🚨 Throws an error! We CANNOT create an object of an Abstract class.

# 🧠 UNDER THE HOOD: Why do we use Abstraction?
# AI EXPLANATION (As requested): 
# Imagine you are a Senior Architect at a Bank. You are writing the `BankApp` core logic, 
# and 5 Junior Developers are writing apps for Mobile, Web, Watch, etc.
# If a junior forgets to write a `security()` function in the Mobile app, hackers will steal the money!
# By making `BankApp` an Abstract Class and `security()` an Abstract Method, you FORCE the junior developers. 
# If they don't write the `security()` method inside `MobileApp`, Python will crash and simply refuse to run their code. 
# It is an "API Contract" that guarantees security and consistency across massive software projects!

# 🌟 ======================================================================= 🌟
#                                     END 
# 🌟 ======================================================================= 🌟
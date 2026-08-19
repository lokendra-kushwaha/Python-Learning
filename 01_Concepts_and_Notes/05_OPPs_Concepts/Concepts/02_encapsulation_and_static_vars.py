# 🌟 ============================================================================================ 🌟
# 🚀                 OOPs --> Classes, Objects, References, Mutability, & Encapsulation
# 🌟 ============================================================================================ 🌟

class Point:

    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return f"<{self.x_cod}, {self.y_cod}>"
    
    def euclidean_distance(self, other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    def distance_from_origin(self):
        return self.euclidean_distance(Point(0, 0))
    

class Line:

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return f"{self.A}x + {self.B}y + {self.C} = 0"
    
    def is_point_on_line(line, point):
        if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:
            return "Lies on the line."
        
        else:
            return "Does not lie on the line."
        
    def shortest_distance(line, point):
        return abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/(line.A**2 + line.B**2)**0.5


    def line_intersect_check(line, other):
        if line.A/other.A != line.B/other.B != line.C/other.C or line.A/other.A != line.B/other.B:
            return "Both lines intersect each other"
        elif line.A/other.A == line.B/other.B == line.C/other.C:
            return "Both lines are overlaping"
        else:
            return "Lines are parallel"


p1 = Point(2, 3)
p2 = Point(3, 4)
print(p1)
print(p2)

print(p1.euclidean_distance(p2))
print(p1.distance_from_origin())

l1 = Line(3, 4, 5)
print(l1)

print(l1.is_point_on_line(p1))
print(l1.shortest_distance(p1))


# 🛠️ ======================================================================= 🛠️
# 🔍 HOW OBJECTS ACCESS ATTRIBUTES -->
# 🛠️ ======================================================================= 🛠️

class Person:

  def __init__(self, name_input, country_input):
    self.name = name_input
    self.country = country_input

  def greet(self):
    if self.country == 'india':
      print('Namaste',self.name)
    else:
      print('Hello',self.name)

    
p = Person('lokendra', 'india')

# 💡 CONCEPT: The object of a class has the power to access the attributes and methods of the class.
print(p.country)
print(p.name)
p.greet()

print(p.gender) # 🚨 throws an error because the person object doesn't have the power to access the gender attribute, as it is not present in the class.

# 💡 CONCEPT: Attribute creation from outside of the class
p.gender = 'male' # attributes can be created outside the class with the help of the object.
print(p.gender)


# 🔗 ======================================================================= 🔗
# 📍 REFERENCE VARIABLE -->
# 🔗 ======================================================================= 🔗

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

p = Person() # object is created
Person('lokendra', 'male') # Object created but not stored in a variable --> Will the object be created? --> Yes, it will be created. (Note: But it will be instantly deleted by Garbage Collector).

p = Person('lokendra', 'male') 
# 🚨 IMPORTANT: 'p' is not an object. Calling Person() creates an object, and we stored its reference in 'p'. 
# 'p' is just a variable that contains the address of the object.
# 'p' is a reference variable.

q = p # now p and q both are variable names pointing to the same address.
print(id(p))
print(id(q))

# The same value will come because both are pointing to the exact same location.
print(p.name)
print(q.name)

# The same value will come because both were pointing to the same object, so making a change via one variable also reflects in the other.
q.name = 'ankit'
print(q.name)
print(p.name)


# 🔄 ======================================================================= 🔄
# 📬 PASS BY REFERENCE --->
# 🔄 ======================================================================= 🔄

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# function --> outside the class not inside
def greet(person):
    print("hi my name is", person.name, "and i am a", person.gender)
    
    p1 = Person('Ankit', 'male') # created another object inside the function
    return p1 # returning p1


p = Person('lokendra', 'male')
greet(p) 
# 💡 CONCEPT: We passed an object to the function as an argument. In Python, this is possible, 
# and the reverse is also possible: a function can return an object of a class.

x = greet(p)
print(x.name) # This can be done because the function is returning a Person class object and it has both attributes.
print(x.gender)


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# Outside the class -> function
def greet(person):
    print(id(person))
    person.name = 'ankit'
    print(person.name)
    print("hi my name is", person.name, "and i am a", person.gender)
    
p = Person('lokendra', 'male')
print(id(p))
greet(p)

# 🎯 CORE LOGIC: The ID of the object inside and outside the function will be exactly the same 
# because technically we don't send the object to the function, rather its address/reference is sent.

print(p.name)
# Both the function and object will print 'ankit'. Because the object we sent was being pointed to by 'p', 
# and we sent it into the function where 'person' received the address. So basically, this also 
# started pointing to the same location. So when we change the name attribute of 'person', obviously 
# changes will reflect in both because both are pointing to the exact same address.


# 🧬 ======================================================================= 🧬
# 🧪 MUTABILITY OF AN OBJECT -->
# 🧬 ======================================================================= 🧬

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# outside the class -> function
def greet(person):
    person.name = 'ankit'
    return person

p = Person('lokendra', 'male')
print(id(p))
p1 = greet(p)
print(id(p1)) 

# 💡 CONCEPT: Even after sending 'p' as an argument to the function and returning the 'person' object from the function, 
# the address of both will remain the same because both are pointing to the same memory location. 
# So making changes will not create another object, rather the changes will happen in the same one. 
# From this, the conclusion is that in Python, classes and objects are mutable. Because when we printed the address of 
# an object created outside the class, and then printed it again after changing the object inside the function, 
# both came out exactly the same. Meaning, even after the object changed, its address remained the same.

# 🎯 CONCLUSION: In Python, user-defined class objects are mutable, just like lists and dicts.

# But they can be made immutable --> I don't know this exactly brother, maybe by making attributes private, well I don't know. 
# (Note: Yes brother! You can make them immutable by overriding the __setattr__ magic method to freeze changes, or by using namedtuples/dataclasses frozen=True).


# 🏷️ ======================================================================= 🏷️
# 👤 WHAT IS INSTANCE VARIABLE IN PYTHON -->
# 🏷️ ======================================================================= 🏷️
class Person:

  def __init__(self, name_input, country_input):
    self.name = name_input # instance variable --> a variable whose value is different for different objects.
    self.country = country_input # instance variable

p1 = Person('lokendra', 'india')
p2 = Person('angela white', 'australia')

print(p1.name)
print(p2.name) 
# 🎯 NOTE: Inside the class, there is only one variable named 'name', but when we created two objects of the class, 
# its value is different for both of them.


# 🛡️ ======================================================================= 🛡️
# 🔒 ENCAPSULATION --->
# 🛡️ ======================================================================= 🛡️
# What is the need? --> 
 
# 🧠 UNDER THE HOOD: Why do we ACTUALLY use Encapsulation in the Industry?
# EXPLANATION (Industry Reality):

# ❌ Textbook Definition: "Encapsulation is hiding data." (Boring & Incomplete)
# ✅ Industry Reality: "Encapsulation is placing a strict Bouncer (Security Guard) outside your data."

# Imagine you are building a Payment Gateway (like Paytm/PhonePe). 
# If your user's balance is a public variable (`user.balance`), a careless frontend developer 
# or a hacker could write a bug like: 
# user.balance = "UNLIMITED" (String) or user.balance = -50000 (Negative int)

# When this string ("UNLIMITED") goes to the database which expects an Integer, 
# the ENTIRE banking server will crash! 

# HOW ENCAPSULATION SAVES THE DAY:
# You make the data private (`__balance`) and create a Setter method (`set_balance`). 
# This Setter acts as a BOUNCER at a nightclub. 
# Before letting the new data touch the actual balance, the Bouncer checks:
# 1. Is it an Integer? (No Strings allowed!)
# 2. Is the amount greater than 0? (No negative money!)
# 
# If the data passes the checking, it gets saved. If a hacker sends "UNLIMITED", 
# the Bouncer throws an Error and the Server is saved from crashing. 
# Encapsulation is not just hiding data; it is taking total CONTROL over how your data is modified!

class Atm:

    def __init__(self):
        print(id(self))
        self.pin = '' 
        self.__balance = 0 # 🚨 putting a double underscore before the variable name makes it private
        # self.menu()


    # 💡 CONCEPT: If we want to give access to an attribute or method but also keep it private:
    # Whenever we make a variable private, its value is not available outside the class, but it IS available inside the class. 
    # Meaning, the methods of the class can access the private data.

    # From here comes the concept of getter and setter. Through them, we can allow access to the value of a private variable from outside the class.
    # getter --> to show the value of a private variable outside.
    # setter --> to get the value of a private variable changed from outside.

    # GETTER
    def get_balance(self):
        return self.__balance
    
    # SETTER
    def set_balance(self, new_value):
        if type(new_value) == int: # We applied a check, now we can only set an int value from outside the class.
            self.__balance = new_value
        else:
            print('beta bahut marenge.') # Son, you will get beaten a lot! 😂

    def __menu(self): # Methods can also be made private. 
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input('Enter your pin: ')
        self.pin = user_pin

        user_balance = int(input('Enter balance: '))
        self.__balance = user_balance

        print('Pin created successfully.')

    def change_pin(self):
        old_pin = input('Enter old pin: ')

        if old_pin == self.pin:
            # let him change the pin
            new_pin = input('Enter new pin: ')
            self.pin = new_pin
            print('Pin change successful')
        else:
            print('Incorrect pin.')

    def check_balance(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.pin:
            print('Your balance is ',self.__balance)
        else:
            print('Incorrect pin.')

    def withdraw(self):
        user_pin = input('Enter the pin: ')
        if user_pin == self.pin:
            # allow to withdraw
            amount = int(input('Enter the amount: '))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print('Withdrawl successful. balance is',self.__balance)
            else:
                print('abe garib') # hey poor guy!
        else:
            print('sale chor') # bloody thief!


# ----------------------- Code before using the concept of private variables -------------------
obj = Atm()

obj.create_pin()
obj.balance = 'hehehe'

# obj.withdraw() # output -> '<=' not supported between instances of 'int' and 'str'
# 🚨 Reason for the error -> Because we changed its variable below the class and put a str value in it.
# Because class attributes can be accessed and changed by the object.

# 🎯 CONCLUSION: Meaning, anyone is able to access and change the class variable, and this is dangerous because if values are changed from outside, the program can crash.
# To avoid this scenario, we use the concept of private attributes.


# ------------------------ Concept of private attributes/variables ----------------------------

obj = Atm()

obj.balance # Now no one can access the attribute named balance from outside the class.

obj.create_pin()
obj.__balance = 'hehehe'

obj.withdraw() 
# But this will not throw an error because the balance attribute is a private variable. Even though its value was changed from outside the class, it won't make any difference inside the class.

# 🧠 NAME MANGLING POST-MORTEM:
# Then what was it when we did obj.__balance = 'hehehe'? --> Whenever a variable is made private, 
# its name changes in the memory and its name becomes 
# (_ClassName__VariableName --> _Atm__balance).

# When we did obj.__balance = 'hehehe', we changed the value of a variable that is in memory. Because of this, another new variable got created in the memory as __balance = 'hehehe', and it has no relation with the class. 
# The variable named balance is present in the memory under the name _Atm__balance.

obj.create_pin()
obj._Atm__balance = 'hehehe'

# obj.withdraw() # Output -> '<=' not supported between instances of 'int' and 'str' --> Because we changed the exact name the private variable was pointing to in memory, which caused its value to change.

# 💡 FUN FACT: In Java, a private variable can never be accessed.
# Then what is the use of the private variable concept if they can be accessed? --> In Python, nothing is truly private.
# Python is a language made for adults. 🤣🤣🤣

# ------------------------------- Testing of getter and setter --------------------------------

obj = Atm()

print(obj.get_balance()) # Output -> 0 : which is the initial value

obj.set_balance(1000)

print(obj.get_balance()) # Output -> 1000 : value got changed

obj.set_balance('hehehe')

print(obj.get_balance())

# obj.withdraw() # Output -> '<=' not supported between instances of 'int' and 'str' --> Because we set a str value via the setter.

# 🎯 What is the benefit of a setter? --> The benefit is that since we created this function and it is inside the class, we can put checks in it for the exact value we want.

obj = Atm()

print(obj.get_balance()) # output -> 0
obj.set_balance('hehehe')
print(obj.get_balance()) # value did not change, it remained 0

obj.set_balance(1000)
print(obj.get_balance()) # value changed because now we set an int value

# 🎯 This exactly is Encapsulation!


# 📦 ======================================================================= 📦
# 🗃️ COLLECTION OF OBJECTS
# 📦 ======================================================================= 📦

class Person:
    def __init__(self, name_input, country_input):
        self.name = name_input
        self.country = country_input

p1 = Person('nitesh', 'india')
p2 = Person('steve', 'australia')
p3 = Person('lokendra', 'india')

l = [p1, p2, p3] # Objects can be stored inside a list and can be treated exactly the way we treat a list object.
print(l)

for i in l:
    print(i)
    print(i.name, i.country)

s = {p1, p2, p3}
print(s) 
# 🚨DOUBT: Don't know why an error didn't come and it got stored, even though we just saw that objects of classes are mutable, but a set only takes immutable data. 
# (Note: Great observation! Objects in Python are "Hashable" by default based on their memory ID. Since their memory ID never changes, the Set accepts them as unique entities).

d = {'p1': p1, 'p2': p2, 'p3': p3}

for i in d:
    print(i)
    print(d[i])
    print(d[i].name)
    print(d[i].country)


# 🏛️ ======================================================================= 🏛️
# 🏗️ STATIC VARIABLES (vs INSTANCE VARIABLES)
# 🏛️ ======================================================================= 🏛️

class Atm:

    __counter = 1 # 💡 Defining static variable

    def init(self):
        self.pin = ''
        self.__balance = 0
        # self.cid = 0 # Instance variable (catching the object's name to use it (self = object))
        # self.cid += 1
        
        self.cid = Atm.__counter # Static variable (catching the class's name to use it)
        Atm.__counter = Atm.__counter + 1
        #self.menu()

    # Utility functions
    @staticmethod # Did this so that it's known that this function belongs to the class and we can call it a utility function.
    def get_counter(): # We can avoid self
        return Atm.__counter


    def get_balance(self):
        return self.__balance

    def set_balance(self,new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print('beta bahot maarenge')

    def __menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input('enter your pin')
        self.pin = user_pin

        user_balance = int(input('enter balance'))
        self.__balance = user_balance

        print('pin created successfully')

    def change_pin(self):
        old_pin = input('enter old pin')

        if old_pin == self.pin:
            # let him change the pin
            new_pin = input('enter new pin')
            self.pin = new_pin
            print('pin change successful')
        else:
            print('nai karne de sakta re baba')

    def check_balance(self):
        user_pin = input('enter your pin')
        if user_pin == self.pin:
            print('your balance is ',self.__balance)
        else:
            print('chal nikal yahan se')

    def withdraw(self):
        user_pin = input('enter the pin')
        if user_pin == self.pin:
        # allow to withdraw
            amount = int(input('enter the amount'))
            if amount <= self.__balance:
                self.balance = self.balance - amount
                print('withdrawl successful.balance is',self.__balance)
            else:
                print('abe garib')
        else:
            print('sale chor')


c1 = Atm()
c2 = Atm()
c3 = Atm()

# print(c1.cid)
# print(c2.cid)
# print(c3.cid) 
# 🎯 CORE LOGIC: The cid of all three is the same, which is 1, because all three objects are at different memory locations 
# and a separate constructor is triggering for all three. And since the value of cid is incrementing by 1 
# within that local scope, the cid of all three customers remained the same.

# 🎯 CONCLUSION --> A counter cannot be implemented using an instance variable.
# This is solved by a static variable, which is a variable of the class, just like an instance variable is a variable of the object.

# 💡 DIFFERENCE: The value of an instance variable is different for every object, whereas the value of a static variable is the same for every object.
# customer name --> should be an instance variable
# bank's IFSC code --> should be a static variable

print(c1.cid)
print(c2.cid)
print(c3.cid) # The cid for all three came out different

Atm.counter = 'hehehe'

# print(c1.cid)
# print(c2.cid)
# print(c3.cid) # 🚨 throws an error -- Output -> can only concatenate str (not "int") to str
# Because we changed the value of the counter to a str
# ---> If we do not want anyone to change the value of the counter, then make it a private variable.

# print(c1.get_counter()) # 🚨 Output -> Atm.get_counter() takes 0 positional arguments but 1 was given
# Because we are sending an object here, but inside the class, the method is not taking any positional arguments.

# Way to access it
print(Atm.get_counter) # This method is called a static method because it belongs to the class, not the object.

# 💡 CONCEPT: Methods are also of two types: 
# 1. Those that don't need any object to be created in order to be accessed (Static Methods).
# 2. Those that need an object because they are methods of the object (Instance Methods).

# 🌟 ======================================================================================== 🌟
#                                    END 
# 🌟 ======================================================================================== 🌟
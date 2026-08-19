# 🚀 OOP Architecture Part 2: Class Relationships, Polymorphism & Abstraction

In Object-Oriented Programming, isolated objects are useless. Real-world applications require objects to communicate, share properties, and enforce rules upon each other. This document explores how classes interact at the architectural level.

---

## 1. Class Relationships: The Big Picture
When designing a system, classes generally interact in two ways:
1. **Aggregation (Has-A Relationship):** One class physically "owns" an object of another class.
2. **Inheritance (Is-A Relationship):** One class chemically "absorbs" the properties of another class.

---

## 2. Aggregation ("Has-A" Relationship)
Aggregation is used when a class contains a complex entity that deserves its own class. For example, a `Customer` "has an" `Address`.

### 📊 Aggregation ASCII Architecture Diagram

     [ Customer Class ]                                       [ Address Class ]
    ---------------------                                    ---------------------
    |   - name          |                                    |     - city        |
    |   - gender        |                                    |     - pin         |
    |   - address: (Obj)|   <>------ (Aggregation) ------    |     - state       |
    |-------------------|                                    |-------------------| 
    | + print_address() |                                    |   + get_city()    |                
    | + edit_profile()  |                                    |   + edit_address()|
    ---------------------                                    ---------------------             
                                              
### 🧠 Under the Hood: The Private Variable Rule
When `Customer` owns the `Address` object, it acts like a remote control. However, **ownership does not mean absolute power.**
* If `__city` is a private variable inside `Address`, the `Customer` class **cannot** access it directly (e.g., `self.address.__city` will crash).
* **The Fix:** The `Address` class must provide a `getter` method. The `Customer` must respectfully ask for the data via `self.address.get_city()`.

---

## 3. Inheritance ("Is-A" Relationship)
Inheritance provides code reusability. A `Student` "is a" `User`. Therefore, `Student` should automatically possess all non-private attributes and methods of `User` without writing them again.

### 📊 Inheritance ASCII Architecture Diagram

    [ Parent: User ]                                            [ Child: Student ]   
    ----------------                                            ------------------
    |   - name     |        <-------- (Inherits) --------       |    - rollno    |
    |--------------|                                            |----------------|
    |   + login()  |                                            |    + enroll()  |
    ----------------                                            ------------------


*Result: The Student object can call `login()` even though it wasn't written inside the Student class.*

### 🚨 The Constructor Overriding Trap
* **Default Behavior:** If the Child class has NO constructor (`__init__`), Python automatically travels up to the Parent class and executes its constructor.
* **The Override:** If the Child class writes its OWN `__init__`, the Parent's `__init__` is **completely ignored**. If the Parent's constructor had important variables (like `self.brand`), they will never be created, causing crashes later.

### 🦸‍♂️ The `super()` Keyword (The Bridge)
To fix the overriding trap, we use `super()`. 
* Placing `super().__init__(price, brand)` inside the Child's constructor explicitly forces Python to execute the Parent's setup logic before completing the Child's setup.
* **Limitations of `super()`:** 
  1. It can ONLY call methods and constructors. It **cannot** directly access variables (`super().brand` throws an error).
  2. It can only be used *inside* a class, never outside.

---

## 4. Multiple Inheritance & The Diamond Problem (MRO)
Python allows a child to have multiple parents (e.g., `class SmartPhone(Phone, Product):`). But what happens if BOTH parents have a method named `buy()`? Which one does the child inherit?

### 🧠 Under the Hood: Method Resolution Order (MRO)
Python uses the **C3 Linearization Algorithm** (often referred to as MRO) to solve this "Diamond Problem."
* **The Rule:** Python reads the inherited classes from **LEFT to RIGHT**.
* Since we wrote `SmartPhone(Phone, Product)`, Python checks `Phone` first. If it finds the `buy()` method there, it executes it and **immediately stops searching**. It will completely ignore the `buy()` method in `Product`.

---

## 5. Polymorphism (Many Forms)
Polymorphism means the exact same code behaves differently depending on the context.

### A. Method Overriding
If a Parent has `buy()` and the Child also has `buy()`, calling `child_object.buy()` will always execute the Child's version. The child "overrides" the parent.

### B. Method Overloading (The Python Workaround)
In languages like Java, you can write two `area()` functions with the same name but different parameters. **Python does not support this.**
* If you write two `area()` functions in Python, the CPython engine simply deletes the first one from memory and only keeps the latest one.
* **The Workaround:** We use default arguments to achieve the same result:

    def area(self, a, b=0):
        if b == 0: return 3.14 * a * a # Circle
        else: return a * b             # Rectangle


### C. Operator Overloading
The exact same operator changes its behavior based on the object's data type (controlled via Magic Methods like `__add__`):
* `"Hello" + "World"` -> Concatenation
* `4 + 5` -> Mathematical Addition

---

## 6. Abstraction (The API Contract)
Abstraction uses the `ABC` (Abstract Base Class) module to hide implementation details and enforce strict rules.

### 🧠 Industry Reality: The Architect vs. Junior Developer
Why do we need Abstraction? Imagine you are a Senior Systems Architect at a Bank. You are writing the core `BankApp` framework, and 5 Junior Developers are building specific apps (Mobile, Web, Watch).

If a junior developer forgets to write a `security()` function in the Mobile app, hackers could breach the system!

**How Abstraction saves the system:**
You create an Abstract Class with an `@abstractmethod` called `security()`.
* **The Rule:** Abstract methods contain no code (`pass`), but they act as a strict **contract**.
* **The Enforcement:** If the junior developer tries to create a `MobileApp` object without writing their own `security()` function, Python will throw a fatal `TypeError` and crash immediately.
* **The Benefit:** Abstraction forces developers to follow a predefined structure. You cannot instantiate an abstract class, and you cannot bypass its rules. It guarantees consistency across massive codebases.
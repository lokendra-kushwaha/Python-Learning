# 🛡️ OOP Architecture: Encapsulation, State & Memory

While Classes and Objects define the physical memory blocks (as seen in `Classes_Objects_and_Lifecycle.md`), this document explores how data is managed, secured, and mutated inside those memory blocks using CPython's internal mechanics.

---

## 1. The Illusion of Variables (Reference Variables)
In Python, variables do not store objects; they store **memory addresses (pointers)**. 

When you write `p = Person()`, two distinct things happen:
1. `Person()` creates a physical object in the RAM.
2. `p` is merely a reference variable that holds the address (e.g., `0x10a2b`) of that object.

**The Multi-Reference Phenomenon:**
If you write `q = p`, Python does not create a new object. It simply copies the memory address from `p` to `q`. Both variables now point to the exact same memory block. Modifying `q.name` will automatically change `p.name` because they are the same physical entity.

---

## 2. Pass by Reference & Object Mutability
By default, all user-defined class objects in Python are **Mutable** (like Lists and Dictionaries).

When you pass an object to a function (`def greet(person):`), you are not sending a copy of the object. You are sending its memory address. 
* Any changes made to the object inside the function (`person.name = 'Ankit'`) will permanently alter the original object outside the function.
* **Under the Hood:** You can verify this by checking `id(original_object)` and `id(passed_object)`. They will always be identical.

---

## 3. State Management: Instance vs. Static Variables
Memory inside an OOP system is divided into two strict scopes:

### A. Instance Variables (Object-Level Memory)
* **Defined via:** `self.variable_name`
* **Architecture:** Stored inside the object's unique dictionary (`__dict__`). 
* **Behavior:** Every object gets its own isolated copy. If `Customer1` changes their name, `Customer2` is unaffected.

### B. Static Variables (Class-Level Memory)
* **Defined via:** Directly inside the class body, accessed via `ClassName.variable_name`.
* **Architecture:** Stored inside the Class blueprint's dictionary, not the object's.
* **Behavior:** Shared across ALL objects. If the class increments a `__counter`, all objects see the updated counter. Ideal for overarching data like Bank IFSC codes or Database Connection Limits.

---

## 4. Encapsulation & Name Mangling (The Security Layer)
Allowing direct access to an object's variables (e.g., `obj.balance = "hehe"`) is an architectural flaw. A user might pass the wrong data type (String instead of Integer) and crash the entire system.

### The Private Variable Myth
To prevent this, we prefix variables with a double underscore (`self.__balance`). However, **nothing is truly private in Python.** Python follows the "Consenting Adults" philosophy.

**The Name Mangling Secret:**
When CPython sees `self.__balance`, it doesn't lock it. Instead, it subtly renames the variable in memory to `_ClassName__VariableName` (e.g., `_Atm__balance`). 
* If a user tries `obj.__balance = 100`, they are simply creating a *new, useless variable* in memory, leaving the actual mangled variable untouched.
* A determined hacker can still access it by calling `obj._Atm__balance`, but this requires intentional bypass, preventing accidental crashes.

*The Bypass (How to access it):* If you absolutely must access or modify the private variable from outside the class, you can use its mangled memory name:
   python
   obj._Atm__balance = "hehe" # This WILL successfully override the private data!
   
This proves that private variables are just a safety mechanism against accidental modification, not a strict security vault against intentional hacking.

---

### Getters and Setters (The Checkpoints)
Since direct access is blocked (or mangled), we provide controlled access via methods:
* **Getter (`get_balance`):** Safely reads and returns the private data.
* **Setter (`set_balance`):** Acts as a security checkpoint. Before updating the private variable, it checks if the incoming data is valid (e.g., `if type(new_value) == int:`). If the check fails, it blocks the mutation.

---

## 5. Method Classification (The Execution Context)
Functions inside a class are classified based on the memory they interact with:

1. **Instance Methods:** Normal methods that take `self` as the first argument. They are used to manipulate Object-Level memory (Instance Variables).
2. **Static Methods (`@staticmethod`):** Utility methods that do not take `self`. They cannot modify object data. They are bound to the Class and are generally used for Class-Level operations or independent logic.
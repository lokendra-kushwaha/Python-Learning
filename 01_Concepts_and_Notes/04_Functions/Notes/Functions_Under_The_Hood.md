# ⚙️ Functions Under The Hood: Objects, Stack Frames & Memory

Most tutorials teach functions simply as "reusable blocks of code." While practically true, this ignores how the CPython interpreter physically manages them in RAM. In Python, functions are not just abstract concepts; they are tangible, physical objects living in your computer's memory.

Let's decode the system architecture of Python functions.

---

## 1. Functions are "First-Class Objects"
In languages like C or Java, a function is fundamentally different from a variable. You cannot assign a C function to a variable or pass it inside an array.

**In Python, a function is just an Object (like a List, Dict, or Integer).**
* When you write `def my_func():`, the `def` keyword is actually an executable command.
* CPython creates a `function` object in the heap memory containing your bytecode.
* It then takes the label (name) `my_func` and attaches it to that memory block.
* **The Superpower:** Because they are just objects, you can assign functions to other variables (`a = my_func`), store them in lists (`[my_func, print]`), or pass them as arguments to other functions.

---

## 2. The Execution Sandbox (The Stack Frame)
What exactly happens when you *call* a function by adding parentheses, like `my_func()`?

1. **The Pause:** The CPython engine pauses the main program's execution.
2. **The Stack Frame (The Temporary Whiteboard):** It creates an isolated, temporary memory workspace called a "Stack Frame" (or Call Stack).
3. **Local Scope Isolation:** Any variable you create *inside* the function (Local Variables) is written entirely on this temporary whiteboard. They do not exist in the main global memory.
4. **The `return` Destruction:** The moment the engine hits the `return` keyword (or the end of the function), it takes the final result, hands it back to the main program, and instantly **destroys and deletes the entire Stack Frame**. All local variables are wiped from RAM forever.

*Architectural Takeaway: This is why you get a `NameError` if you try to print a function's inner variable from the outside. That memory literally does not exist anymore!*

---

## 3. The Myth of "Pass by Value" vs. "Pass by Reference"
This is a classic interview trap. If you pass a variable into a function (`my_func(x)`), does Python copy the value (Pass by Value like C) or pass the memory pointer (Pass by Reference like C++)?

**Python does neither. It uses "Pass by Object Reference" (or Pass by Assignment).**

Remember our "Boxes vs. Labels" concept? 
* When you pass a variable into a function, Python does **not** copy the data.
* It simply creates a **new Label** (the function's parameter name) and sticks it onto the exact same underlying object in memory.

**The Mutability Trap:**
* If you pass an **Immutable** object (like an `int` or `string`), and the function tries to change it, Python just creates a new object locally. The original data outside remains safe.
* If you pass a **Mutable** object (like a `list` or `dict`), the function's label is pointing to the exact same memory array as the outside code. If the function runs `.append()`, the original list outside the function **will be permanently modified!**
# 🗂️ Namespaces & Scope: The Dictionary Secret

While "Scope" (LEGB) defines *where* a variable can be accessed, "Namespace" defines *how* it is physically stored in memory. Understanding the connection between the two is crucial for mastering Python's memory architecture.

---

## 1. What is a Namespace? (The Secret Dictionary)
In C/C++, variable names are compiled down to raw memory addresses, and the names themselves disappear. 
In Python, variable names survive the compilation process. A **Namespace** is simply a system that maps these human-readable variable names to their actual object memory addresses.

**The CPython Reality:** Under the hood, a Namespace is literally just a standard Python Dictionary (`dict`). 
* The **Key** is the variable name as a string (e.g., `"x"`).
* The **Value** is the memory reference to the object (e.g., `<int object at 0x10a2b>`).

You can actually see these raw dictionaries by calling the built-in functions `globals()` or `locals()` in your code!

---

## 2. Connecting Namespaces to the LEGB Rule
Since Namespaces are just dictionaries, the **LEGB Rule** is simply the internal search algorithm CPython uses to query these dictionaries in a specific sequence:

1. **Local Namespace (L):** When you query a variable, Python first calls `locals()` inside the current Stack Frame. If the key exists in this dictionary, it stops searching.
2. **Enclosing Namespace (E):** If not found, it checks the `locals()` dictionary of any parent functions (if nested).
3. **Global Namespace (G):** If still not found, it queries the `globals()` dictionary of the entire module/script.
4. **Built-in Namespace (B):** Finally, it checks the `__builtins__` module dictionary, which contains core Python functions like `print` and `len`.

---
> **💡 Engineering Takeaway:** When you write `x = 10` globally, you are just doing `globals()['x'] = 10` behind the scenes. The LEGB rule is just a sequence of dictionary lookups (`dict.get()`) that the CPython engine performs to find your data.
# ⚙️ Python Functions: Memory, Scope & Architecture

Welcome to the **Functions** module. Here, we document functions not just as reusable code blocks, but as physical objects managed within the computer's memory.

### 📂 Folder Structure

This module is organized into practical implementations and deep-dive architectural theory notes.

* **`src/` (Practical Code)**
  * `01_functions_in_python.py`: Code examples demonstrating function creation, execution, and core mechanics.

* **`docs/` (System Architecture)**
  * `Args_and_Kwargs_Under_The_Hood.md`: How the engine dynamically packs arguments into Tuples and Dictionaries.
  * `Functions_Under_The_Hood.md`: Functions as First-Class Objects, the Call Stack, and Pass by Object Reference.
  * `Higher_Order_Functions.md`: Functions that accept or return other functions.
  * `Namespaces_Architecture.md`: The dictionary secret behind variable storage.
  * `Scope_Closures_Lambda.md`: The LEGB rule, garbage collection traps (Closures), and anonymous functions.

### 🧠 Architectural Concepts Covered

* **Functions as First-Class Objects:** Understanding that a function is a memory label that can be passed around, leading to **Higher-Order Functions**.
* **The Call Stack & Stack Frames:** How Python creates a temporary sandbox memory when a function is called, and destroys it when the function returns.
* **Pass by Object Reference:** How Python passes "Memory Labels" instead of passing by value or reference.
* **Memory Packers (`*args` & `**kwargs`):** How the CPython engine dynamically packs leftover arguments into memory-efficient **Tuples** and **Dictionaries**.
* **Namespaces & The LEGB Rule:** Exploring Namespaces as standard Python Dictionaries behind the scenes, and LEGB as the strict 4-step search algorithm.
* **Closures & Lambdas:** How nested functions can trap memory variables to survive Garbage Collection (Closures), and how to write anonymous, single-line functions (Lambdas).
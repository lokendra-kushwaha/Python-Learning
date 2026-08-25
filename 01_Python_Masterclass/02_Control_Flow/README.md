# 🔀 Python Control Flow (Under The Hood)

Welcome to the **Control Flow** module. In this folder, we explore how the **CPython engine** evaluates conditions, jumps across memory addresses, and controls the execution path of the code.

### 📂 Folder Structure

This module is organized into two main sections: practical implementations and architectural theory.

* **`src/` (Practical Code)**
  * `01_if_else_and_match_case.py`: Code examples demonstrating conditional logic and the modern `match-case` statement.
  * `02_loops.py`: Practical scripts exploring `for` and `while` loop mechanics.

* **`docs/` (System Architecture)**
  * `Control_Flow_Architecture.md`: A deep dive into how CPython handles control flow under the hood.

### 🧠 Architectural Concepts Covered

* **The "Truthy & Falsy" Evaluation:** How Python skips explicit boolean calculations (`== True`) and directly checks if a memory object is "empty" or "zero" to make fast decisions.
* **The "For Loop" Mechanics:** Understanding that Python's `for` loop relies on iterators (`__next__()`) and error handling (`StopIteration`) under the hood.
* **Control Statements (`break`, `continue`, `pass`):** How we command the CPU to terminate a loop, skip an iteration, or perform a "No Operation" (NOP) in machine code.

---
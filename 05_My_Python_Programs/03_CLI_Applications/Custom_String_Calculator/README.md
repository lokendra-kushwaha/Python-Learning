# 🧮 Custom String Parser Calculator

A terminal-based calculator built using "First Principles Thinking". Instead of relying on Python's built-in `eval()` function or math modules, this application manually parses mathematical strings and computes the results using core logic.

## 🚀 The Core Logic
When a user inputs a string like `9+5+2`, the program doesn't execute it directly. Instead, it:
1. Splits the string by the operator (e.g., `+`).
2. Cleans up edge cases (like trailing or leading operators: `+9+5+`).
3. Converts the string array into integers.
4. Uses Python's `functools.reduce()` alongside a `lambda` function to continuously apply the operation across the entire list.

## ✨ Key Features
* **Zero Dependencies:** Pure Python logic without external mathematical libraries.
* **Edge Case Handling:** Intelligently manages rogue operators entered by the user (e.g., `-9-5-`).
* **Robust Error Management:** Implements `try-except` blocks to catch `ValueError` (if alphabets are entered) and `ZeroDivisionError` (to prevent crashes during division by zero).
* **Google-Style Docstrings:** Fully documented functions for easy reading and maintenance.

## 💻 How to Run
Simply execute the script in your terminal and select your desired operation:
```bash
python calculator.py
```
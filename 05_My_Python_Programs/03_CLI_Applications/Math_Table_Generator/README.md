# 🔢 CLI Math Table Generator

A simple and interactive Command Line Interface application that acts as a mathematical assistant to generate multiplication tables on the fly.

## 💡 How It Works
The user provides a base number, and the program instantly generates its multiplication table (from 1 to 10). Afterwards, the user is prompted to fetch a specific multiple (e.g., the 4th multiple of the given number) from that table.

## 🛠️ Code Features & Learnings
* **Looping:** Utilizes a standard `for i in range(1, 11)` loop to iterate and print the mathematical calculations dynamically.
* **Pattern Matching:** Implements Python's `match-case` to handle user queries for specific multiples. 
* **String Formatting & Grammar Logic:** The pattern matching block is structured to apply the correct ordinal English suffixes (1st, 2nd, 3rd, and grouping 4th-10th) when printing the final result.
* **Continuous Execution:** Wrapped in a `while True` loop to ensure the user can generate as many tables as they want without restarting the script.
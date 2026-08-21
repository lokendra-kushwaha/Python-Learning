# 🧠 CLI Quiz Application

A Python terminal-based Multiple Choice Question (MCQ) quiz game. The game tests the user's general knowledge and features an interactive input validation system.

## 🎮 Game Modes
The user can select between two scoring systems before starting the quiz:
1. **Normal Mode:** Standard scoring. `+1` for a correct answer, `0` for a wrong answer.
2. **Hard Mode:** Competitive exam style scoring. `+1` for a correct answer, `-1/3` (negative marking) for a wrong answer.

## 🧠 Technical & Mathematical Highlights
* **Data Structures:** Uses a Python Dictionary `{'Question': 'Answer'}` to store and iterate through the quiz data seamlessly.
* **Input Sanitization:** Uses nested `while True` loops to ensure the game never crashes due to an invalid user input.
* **Algorithmic Math Trick (Hard Mode):** Instead of keeping two separate counters for positive and negative marks, the code uses a mathematical shortcut. For every wrong answer, it adds a penalty of `4/3` (which represents the `1` mark lost + `1/3` negative mark). The final score is simply calculated as `Total Questions - Penalty`.
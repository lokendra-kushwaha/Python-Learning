# 🏦 Basic ATM Simulation

A classic beginner-friendly Python mini-project that simulates a real-world ATM interface. 

## 💡 About The Project
This project was built to practice control flow and state management in Python. It provides a terminal-based menu where users can check their balance, withdraw money, or deposit cash. 

## 🛠️ Technical Highlights
* **Continuous Execution:** Built using an infinite `while True` loop, allowing the user to perform multiple transactions without the program terminating abruptly. The loop only breaks when the user explicitly chooses the 'Exit' option.
* **State Management:** The `balance` variable is strategically declared *outside* the loop. This ensures that the state of the user's bank account persists and updates correctly across multiple withdrawals and deposits during the same session.
* **Control Flow:** Utilizes clean `if-elif-else` logic to handle user menu choices and basic validation (e.g., ensuring withdrawal amounts don't exceed the current balance).

**Lesson Learned:** A great early exercise in understanding how variables act as memory in a running application!
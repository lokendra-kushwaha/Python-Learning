# ⏱️ Daily Study Hours Tracker

A productivity CLI tool built to log daily study sessions and track them against a set 10-hour daily target.

## 💡 Features
Users can log their study hours iteratively. The program accumulates the total time and provides a final breakdown, calculating exactly how many hours are left to reach the goal.

## 🛠️ Logic & Learning
* **Accumulator Pattern:** Demonstrates the classic use of an accumulator variable (`total_hours += hours`) inside a `while` loop.
* **Data Type Handling:** Upgraded from integers to floats to accurately track fractional hours (e.g., 1.5 hours of study).
* **Conditional Feedback:** Uses clean `if-else` logic at the end of the session to calculate remaining hours or congratulate the user upon hitting their target.
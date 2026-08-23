# 🏋️‍♂️ Weekly Workout Planner (CLI)

A simple and interactive Command Line Interface utility designed to help track and display a weekly workout routine. 

## 💡 What It Does
The user simply enters a day of the week (1-7), and the application instantly fetches the specific workout split for that day (e.g., Upper Body, Core, Yoga). It runs on a continuous loop until the user decides to exit.

## 🛠️ Technical Highlights
* **Structural Pattern Matching:** Built using Python 3.10's `match-case` syntax to replace multiple `if-elif` blocks, making the code much cleaner and more readable.
* **Continuous Flow:** Uses an infinite `while True` loop with a clear `exit` condition to keep the user engaged without needing to restart the script repeatedly.
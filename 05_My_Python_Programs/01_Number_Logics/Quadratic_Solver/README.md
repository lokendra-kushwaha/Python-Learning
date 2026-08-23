# 🧮 OOP Quadratic Equation Solver

This folder contains a milestone script in my programming journey: my first steps into Object-Oriented Programming (OOP) applied to a complex mathematical concept.

## 💡 The Objective
To create a Python `class` that not only stores the coefficients ($a$, $b$, and $c$) of a quadratic equation but also possesses the ability to print itself mathematically and calculate its fractional factors.

## 🛠️ Technical Highlights
* **OOP Fundamentals:** Utilizes `__init__` for instantiation and `__str__` to return a human-readable format of the equation (e.g., `2x² + 5x + 2 = 0`).
* **The Formatting:** When calculating the roots using the standard quadratic formula $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$, negative numbers often mess up the display format of factors (e.g., `(4x - -2)`). This script uses a brilliant brute-force string method `.replace('- -', '+ ')` to clean up the math layout on the fly!